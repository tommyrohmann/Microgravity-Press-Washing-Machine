/*
Microgravity Press Washing Machine MicroController Code
Tommy Rohmann
2026

This code receives state machine inscructions via the serial bus and actuates these commands until a specified
condition is met, and sends sensor telemetry back through the serial bus upon request.

This code is workable to where individual commands can be sent over the serial bus manually,
and instructions not matching the list of I/O addresses or the correct format are not used by the machine,
Instructions can be followed with or without the use of control endpoints,
and can be executed in a direct actuation of instructions, or through a stepped actuation,
which allows for safe transition between actuating previous and currect instruction sets.
*/

#include <iostream>
#include <map>
#include <string>
#include <variant>
#include <vector>
#include <ESP32Servo.h>

//Naming Servos
Servo oVA;
Servo oVR1;
Servo oVR2;
Servo oVWC;
Servo oVWI;
Servo oVSO;
Servo oVRT;
Servo oVCT;

//Setting Pins I/O
const int oVA_pin = 32;   //Air Valve
const int oVR1_pin = 33;  //Wash Pump Direction Reversal Valve 1
const int oVR2_pin = 25;  //Wash Pump Direction Reversal Valve 2
const int oVWC_pin = 26;  //Wash Chamber Valve
const int oVWI_pin = 27;  //Clean Water Input Valve
const int oVSO_pin = 14;  //Soiled Water Output Valve
const int oVRT_pin = 12;  //Retention Tank Valve
const int oVCT_pin = 13;  //Compression Tank Valve
const int oPW_pin = 21;   //Wash Pump
const int oPV_pin = 22;   //Vacuum Pump
const int oPD_pin = 18;   //Detergent Pump
const int oVB_pin = 23;   //Valve Power Bus

const int iES_pin = 35;   //E-Stop Signal
const int iPT1_pin = 39;  //Pressure Transducer
const int iPT2_pin = 36;  //Pressure Transducer

double endTime = 0;

//Sensor Calibration, converts voltage range reading to pressure (Bar)
/*
  note, there should be a variable for each sensor, but the gauges used to calibrate these sensors do not
  even agree when reading the same pressure, so really this is an estimation which will get both sensors close
  to the correct reading. This really only serves a purpose of making wash instructions and telemetry understandable to read, write, and interpret.

  All sensor endpoints are found experimentally by seeing how much vacuum or pressure is attainable by equipement, or wanted by the user anyways.

  Having individual configuration variables, and a calibration function is something worth looking into in future iterations
*/
double PressMultiplier = 432;
double PressOffset = 349;

//map initialization for instruction set
std::map<std::string, std::vector<std::string>> instructions{
  //Instruction Type
  { "IT", { "PIB" } },
  { "TR", { "F" } },
  //Valve Positions
  { "oVA", { "S" } },
  { "oVR1", { "F" } },
  { "oVR2", { "F" } },
  { "oVWC", { "C" } },
  { "oVWI", { "C" } },
  { "oVSO", { "C" } },
  { "oVRT", { "C" } },
  { "oVCT", { "C" } },
  { "oVCT", { "C" } },
  //Relay Outputs
  { "oPW", { "0" } },
  { "oPV", { "0" } },
  { "oPD", { "0" } },
  { "oVB", { "0" } },
  //End Condition
  {"S1", {"iTd","<","0"}},
  {"S2", {"iTd","<","0"}},
  {"E1", {"iTd","<","0"}}
};

//map initialization for previous instruction save, used by SafeSequenceActuateInstructions to minimize opening and closing valves while preserving conditions in chambers in transient period between executing instructions
std::map<std::string, std::vector<std::string>> prevInstructions = instructions;

//Default Safe State, machine will return to this safe state if instructions are not received once an end state is met in a predetermined amount of time
std::map<std::string, std::vector<std::string>> Safe_State{
  //Instruction Type
  { "IT", { "PI" } },
  { "TR", { "F" } },
  //Valve Positions
  { "oVA", { "S" } },
  { "oVWI", { "C" } },
  //Relay Outputs
  { "oPW", { "0" } },
  { "oPV", { "0" } },
  { "oPD", { "0" } },
  { "oVB", { "0" } },
  //Endpoints
  {"S1", {"iTd","<","0"}},
  {"S2", {"iTd","<","0"}},
  {"E1", {"iTd","<","0"}}
};

//Map initialization for used Sensor States to print as telemetry (Also shows what variable/name corresponds to on machine)
std::map<std::string, double> SensorStates{
  {"iPT1",0}, //Wash Chamber Side Pressure Sensor
  {"iPT2",0}, //Reservoir Side Pressure Sensor
  {"iT",0}, //microcontroller time
  {"iTd",0}, //Instruction dT
  {"iTS",0}, //Start Time of Instruction
  {"iES",0}, //EMCY STOP
  {"ECM",0}, //End Condition Met
};

//set up pin locations, pin modes, and starts serial bus on boot
void setup() {
  Serial.begin(115200);
  while (!Serial) {
    delay(10);
  }

  oVA.attach(oVA_pin);
  oVR1.attach(oVR1_pin);
  oVR2.attach(oVR2_pin);
  oVWC.attach(oVWC_pin);
  oVWI.attach(oVWI_pin);
  oVSO.attach(oVSO_pin);
  oVRT.attach(oVRT_pin);
  oVCT.attach(oVCT_pin);
  pinMode(oPW_pin, OUTPUT);
  pinMode(oPV_pin, OUTPUT);
  pinMode(oPD_pin, OUTPUT);
  pinMode(oVB_pin, OUTPUT);

  analogReadResolution(12);  //ESP32 ADC setup, 0-4095
  pinMode(iES_pin, INPUT);
  Serial.println("SETUP Finished");
}

//used for troubleshooting, prints out instructions to serial port to find state of port
void TroubleshootPrintInstructions(const std::map<std::string, std::vector<std::string>>& a){
      // Print the map
    for (const auto& [key, values] : a)
    {
        Serial.print(key.c_str());// + " : ");
        Serial.print(":");

        for (const std::string& value : values)
        {
            Serial.print(value.c_str());//+",");
            Serial.print(";");
        }

    }
    Serial.println("");
}

//All Valves have a similar set of positions, This function maps a valve position symbol to a servo position, and sends the command for the servo to move
void Configure_Valve(std::string Target, Servo& Selected_Servo, const std::map<std::string, std::vector<std::string>>& a) {
  //find instruction based on target title
  auto it = a.find(Target);

  //Anti-crash checks
  if (it == a.end()) {
    return;
  }
  if (it->second.empty()) {
    return;
  }
  std::string value = it->second[0];

  int angle = 0;

  //Valve Positions of Various Valves
  if (value == "F") {
    angle = 180;
  } else if (value == "R") {
    angle = 0;
  } else if (value == "C") {
    angle = 80;
  } else if (value == "O") {
    angle = 0;
  } else if (value == "A") {
    angle = 0;
  } else if (value == "S") {
    angle = 90;
  } else if (value == "V") {
    angle = 180;
  } else {
    return;
  }

  Selected_Servo.write(angle);
}

//Read the contents of an instruction string
std::map<std::string, std::vector<std::string>> ReadCommand(std::string x) {
  std::map<std::string, std::vector<std::string>> instructions{};

  // Separate command into individual instructions using ';'
  int start = 0;

  while (start < x.length()) {
    //find ;
    int end = x.find(';', start);

    if (end == std::string::npos)
      break;

    std::string item = x.substr(start, end - start);

    // Find ':'
    size_t delimiter = item.find(':');

    if (delimiter != std::string::npos) {
      std::string key = item.substr(0, delimiter);
      std::string value = item.substr(delimiter + 1);

      // Separate values using ','
      std::vector<std::string> values;

      int valueStart = 0;

      while (valueStart < value.length()) {
        int comma = value.find(',', valueStart);

        if (comma == std::string::npos) {
          // Last value
          values.push_back(value.substr(valueStart));
          break;
        }

        values.push_back(value.substr(valueStart, comma - valueStart));

        valueStart = comma + 1;
      }

      instructions[key] = values;
    }

    start = end + 1;
  }

  return instructions;
}

//Read Sensor Values
void Read_Sensors(){
  SensorStates["iES"] = digitalRead(iES_pin); //E-Stop Signal
  SensorStates["iPT1"] = (analogRead(iPT1_pin)-PressOffset)/PressMultiplier;
  SensorStates["iPT2"] = (analogRead(iPT2_pin)-PressOffset)/PressMultiplier; //List of things to send over string, include data format info for python data logger
  SensorStates["iT"] = millis(); //microcontroller time
  SensorStates["iTd"] = SensorStates["iT"]-SensorStates["iTS"]; //Instruction dT
}

//Check if the end state conditions have been met for a given instruction set
void CheckStopConditions(std::vector<std::string> StopCondition,int ConditionType) {
  if (SensorStates["ECM"] == 0){
    std::string a = StopCondition[0]; //Target
    std::string b = StopCondition[1]; //Relationship
    double c = std::stod(StopCondition[2]); //Value

    if (b=="<" && SensorStates[a] < c){
    SensorStates["ECM"] = ConditionType;
    }  else if (b==">" && SensorStates[a] > c){
    SensorStates["ECM"] = ConditionType;
    }
  }
}

//Instruction to Simplify Actuate Instructions Function
void Do_Digital_Output(std::string Target, int Pin, const std::map<std::string, std::vector<std::string>>& a) {
  if (a.find(Target) != a.end()) {
    if (a.at(Target)[0] == "1") {
      digitalWrite(Pin, HIGH);
    }
    if (a.at(Target)[0] == "0") {
      digitalWrite(Pin, LOW);
    }
  }
}

//Function sets output values of various given instruction types
void ActuateInstructions(const std::map<std::string, std::vector<std::string>>& a) {
  auto x = a;
  Do_Digital_Output("oPW", oPW_pin, x);  //Wash Pump
  Do_Digital_Output("oPV", oPV_pin, x);  //Vacuum Pump
  Do_Digital_Output("oPD", oPD_pin, x);  //Detergent Pump
  Do_Digital_Output("oVB", oVB_pin, x);  //Valve Bus

  Configure_Valve("oVA", oVA, x);
  Configure_Valve("oVR1", oVR1, x);
  Configure_Valve("oVR2", oVR2, x);
  Configure_Valve("oVWC", oVWC, x);
  Configure_Valve("oVWI", oVWI, x);
  Configure_Valve("oVSO", oVSO, x);
  Configure_Valve("oVRT", oVRT, x);
  Configure_Valve("oVCT", oVCT, x);
}

//Actuates machine outputs in a predetermined safe sequence
void SafeSequenceActuateInstructions(const std::map<std::string, std::vector<std::string>>& a){
  /*This function safely transitions from the previous instruction set to the new one,
  ensuring preservation of chamber pressures and minimizing losses by following an order of instruction execution
  all while minimizing opening and closing valves redundantly, and minimizing time where the valve bus is energized
  This is done through the following steps:
  1) closing valves to be closed, allowing time for them to close
  2) opening valves to be opened
  3) Starting required pumps

  Timing of stepped execution is accomplished by tracking stepped instruciton time, iTd
  */
  std::map<std::string, std::vector<std::string>> steppedInstructions = prevInstructions;
  steppedInstructions.at("oPW")[0]="0";
  steppedInstructions.at("oPV")[0]="0";
  steppedInstructions.at("oPD")[0]="0";
  steppedInstructions.at("oVB")[0]="1";

  //close Valves to be closed
  if (SensorStates.at("iTd")<5000){
  
  //TroubleshootPrintInstructions(prevInstructions);
  //IT:PI;TR:T;oVA:S;oVR1:F;oVR2:F;oVWC:C;oVWI:C;oVSO:C;oVRT:C;oVCT:C;
  //IT:PI;oVWC:O;oVCT:C;
  //IT:PI;oVWC:C;oVCT:O;

      for (auto const& [key, val] : a){
        //Check if any instructions correspond to a valve being closed, no nameing conflict with other instruction types
        if (val[0] == "C" || val[0] == "S"){
          steppedInstructions.at(key)[0] = val[0];
      }
    }
    //TroubleshootPrintInstructions(steppedInstructions);
  }

  //Open Valves to be opened
  if (SensorStates.at("iTd")>2500 && SensorStates.at("iTd")<5000){
      for (auto const& [key, val] : instructions){
        //Check if any instructions correspond to a valve being open, no nameing conflict with other instruction types
        if (val[0] == "O" || val[0] == "A" || val[0] == "V" || val[0] == "F" || val[0] == "R"){
          steppedInstructions.at(key)[0] = val[0];
      }
  }
  //TroubleshootPrintInstructions(steppedInstructions);
  }

  //Valves no longer being adjusted, valve bus de-energized, energize required pump relays
  if (SensorStates.at("iTd")>5000-1){
    steppedInstructions = a;
    steppedInstructions.at("oVB")[0]="0";
  }
  
  //steppedInstructions.at("oPV")[0]="0";
  ActuateInstructions(steppedInstructions);
  //TroubleshootPrintInstructions(steppedInstructions);

  //IT:PI;TR:T;oVA:S;oVR1:F;oVR2:F;oVWC:C;oVWI:C;oVSO:C;oVRT:C;oVCT:C;
  //IT:PI;TR:T;oVWC:O;oVCT:O;oVRT:C;oPW:0;
  //IT:PI;TR:T;oVWC:O;oVCT:C;oVRT:O;oPW:1;
}

//Clears enpoints between instruction phases being received
std::map<std::string, std::vector<std::string>> ClearEndpoints(const std::map<std::string, std::vector<std::string>>& a){
  /*
  State endpoints should not be preserved between instructions to avoid inadvertant premature termination of phase.
  //This can occur if an endpoint used is not replaced by a new enpoint in the next set of instructions
  //This function replaces all endpoints, which in the communication protocol is an instruction item with more than 1 component in the vector,
  with an endpoint condition which is impossible to be reached
  */
  std::map<std::string, std::vector<std::string>> ClearedEndpoints = a;
  std::vector<std::string> impossibleEndpoint={"Target",">","600000"}; //not impossible, but a given phase probably shouldn't run for more than 10 minutes

  for (auto const& [key, val] : a){
        //Check if any instructions correspond to an end point
        if (val.size()>2){
          //Check if that endpoint is contained in the incoming instructions, if it isn't present, replace with impossible string
            ClearedEndpoints[key] = impossibleEndpoint;
            ClearedEndpoints.at(key)[0]=a.at(key)[0];
      }
    }
    //TroubleshootPrintInstructions(ClearedEndpoints);
    return ClearedEndpoints;
}

void SendTelemetry(std::map<std::string, double> x){
    std::string telemetry = "";
    for (auto const& [key, val] : x){
        telemetry += key + ":" + std::to_string(val) + ";";
    }

  Serial.println(telemetry.c_str());
}

void loop() {
  //Check for New Instructions and Read
  if (Serial.available()) {
    prevInstructions = instructions; //Save record of previous instructions

    //Read Serial Bus and interpret new command in usable map-vector format
    auto receivedInstructions = ReadCommand(Serial.readStringUntil('\n').c_str());

    //if Telemetry is not requested, clear endpoints
    if (receivedInstructions.at("TR")[0]!="T"){//&& receivedInstructions.size()<2){
      instructions = ClearEndpoints(instructions); //Clear old endpoints
    }

    int instructCount=0;
    //Overwrite instructions received over old instructions, preserving old where not specified
    for (const auto& entry : receivedInstructions) {
    instructions[entry.first] = entry.second;
    instructCount+=1;
  }

    //Configure inputs and markers to match beginning of new instruction set
    if (instructions.at("TR")[0]=="F" || instructCount > 1){
    SensorStates["ECM"] = 0; //end condition met marker set to 0 or false
    SensorStates["iTS"] = millis(); 
    endTime = 0; //Impossible end time condition, Just makes it so end time doesnt update until end state is met the first time, and only the first time
    //Debug//TroubleshootPrintInstructions(instructions);
    }
    //Debug //Serial.println(instructions.at("IT")[0].c_str());
  }

  //Basic Instruction read just executes the instruciton code
  if (instructions.at("IT")[0]=="PIB"){
    ActuateInstructions(instructions);
  }

  //Instruction Read Follows Safe State
  if (instructions.at("IT")[0]=="PI"){
    SafeSequenceActuateInstructions(instructions);
    //Follow with stepped valve closing and opening
  }

  //Read Sensors
  Read_Sensors();

  //Check Sensor Output against stop conditions
  CheckStopConditions(instructions.at("S1"),1);
  CheckStopConditions(instructions.at("S2"),1);
  CheckStopConditions(instructions.at("E1"),2);

  //Read Sensors and Print readout to Serial Bus
  if (instructions.at("TR")[0]=="T"){
    SendTelemetry(SensorStates);
    instructions.at("TR")[0]="F";
  }

//finds the time the end state has been met only when it occurs
  if (SensorStates["ECM"]!=0){
    //Immediately shut off pumps at end of end state
    instructions.at("oPW")[0]="0";
    instructions.at("oPV")[0]="0";
    instructions.at("oPD")[0]="0";
    instructions.at("oVB")[0]="0";
    if (endTime == 0){
      endTime = millis();
    }

  }

//checks if the microcontroller has been waiting in the end condition for more than 10 seconds, when this happens it goes to a safe state.
  if (SensorStates["ECM"]!=0 && millis()-endTime > 10000){
    instructions = Safe_State;  
    //instructions.at("TR")[0]="T";
    //Serial.println(millis()-endTime);
    
  }
  delay(1); //Arbitrary delay time between loop cycles
}

//Debug Comment*/

//Below is a lest of test communications used for calibration, verifying component operation, and determining if various functions work as intented
/*
  //List of commands to copy and paste from during troubleshooting
  //oVA:A;oVR1:F;oVR2:F;oVWC:O;oVWI:O;oVSO:O;oVRT:O;oVCT:O;
  //oVA:S;oVR1:F;oVR2:F;oVWC:C;oVWI:C;oVSO:C;oVRT:C;oVCT:C;
  //oVB:0;
  //oVR1:F;oVR2:F;oVB:1;
  //oVR1:R;oVR2:R;oVB:1;
  //oPW:1;
  //oPV:1;
  //oVA:S;
  //oVWI:C;oVSO:C;oVB:1;
  //oVWI:O;oVSO:C;oVRT:O;oVCT:C;oVWC:C;oVB:1;

  //End State Testing
  IT:PI;oVB:1;TR:T;S1:iTd,>,15000;oPV:1;
  oVB:0;TR:T;

  //Test of sequenced instruction actuation, IT:PI
  IT:PI;TR:T;oVA:S;oVR1:F;oVR2:F;oVWC:C;oVWI:C;oVSO:C;oVRT:C;oVCT:C;

  IT:PI;TR:T;oVWC:O;oVCT:O;oVRT:C;oPV:0;
  IT:PI;TR:T;oVWC:O;oVCT:C;oVRT:O;oPV:1;

  IT:PI;oVWC:O;oVCT:C;
  IT:PI;oVWC:C;oVCT:O;

  //Evacuate Wash Chamber Fully
  
  IT:PI;TR:T;oVWC:O;oVCT:O;oVRT:C;oVA:V;oPV:1;
  TR:T;
  IT:PI;oPV:0;
//*/
