#include <iostream>
#include <map>
#include <string>
#include <variant>
#include <vector>
#include <ESP32Servo.h>

bool new_instructions;

Servo oVA;
Servo oVR1;
Servo oVR2;
Servo oVWC;
Servo oVWI;
Servo oVSO;
Servo oVRT;
Servo oVCT;

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

double iT = 0;   //total elapsed time from esp32 start
double iTS = 0;   //start time of 
double idT = 0;  //Change in time

char EndConditionMet = "F"; //T, F, E for true, false, and emergency

//Default Safe State
std::map<std::string, std::vector<std::string>> instructions{
  //Instruction Type
  { "IT", { "PI" } },
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
  { "oVB", { "1" } },
  //
};

//Default Safe State
std::map<std::string, std::vector<std::string>> Safe_State{
  //Instruction Type
  { "IT", { "PI" } },
  //Valve Positions
  { "oVA", { "S" } },
  { "oVWI", { "C" } },
  //Relay Outputs
  { "oPW", { "0" } },
  { "oPV", { "0" } },
  { "oPD", { "0" } },
  //
};

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
}

void Configure_Valve(std::string Target, Servo& Selected_Servo) {
  //find instruction based on target title
  auto it = instructions.find(Target);

  //Anti-crash checks
  if (it == instructions.end()) {
    return;
  }
  if (it->second.empty()) {
    return;
  }
  std::string value = it->second[0];

  int angle = 0;

  if (value == "F") {
    angle = 0;
  } else if (value == "R") {
    angle = 180;
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

std::map<std::string, std::vector<std::string>> ReadCommand(std::string x) {
  std::map<std::string, std::vector<std::string>> instructions{};

  // Separate command into individual instructions using ';'
  int start = 0;

  while (start < x.length()) {
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

char CheckStopConditions(vector StopCondition, char Condition_Type) {
  //CT = Condition Type
  a = StopCondition[0]; //Target
  b = StopCondition[1]; //Relationship
  c = StopCondition[2]; //Value
  
  if (b="<" && a<c){
    return Condition_Type;
  }
  elif (b=">" && a>c){
  //check each sensor output and boolean by instructions, if condition is met
    return Condition_Type;
  }
  else{
    return "f"
  }
}

String Read_Sensors(){
  String Telemetry = ""
  //append values to new string
  EndConditionMet;
  analogRead(iPT1_pin);  //Pressure Transducer
  analogRead(iPT2_pin);  //Pressure Transducer
  iT;
  iTd;
  iTS;
  return Telemetry;
  
}


void Do_Digital_Output(std::string Target, int Pin) {
  if (instructions.find(Target) != instructions.end()) {
    if (instructions.at(Target)[0] == "1") {
      digitalWrite(Pin, HIGH);
    }
    if (instructions.at(Target)[0] == "0") {
      digitalWrite(Pin, LOW);
    }
  }
}

void ActuateInstructions(const std::map<std::string, std::vector<std::string>>& instructions) {
  Do_Digital_Output("oPW", oPW_pin);  //Wash Pump
  Do_Digital_Output("oPV", oPV_pin);  //Vacuum Pump
  Do_Digital_Output("oPD", oPD_pin);  //Detergent Pump
  Do_Digital_Output("oVB", oVB_pin);  //Valve Bus

  //oVA:A;oVR1:F;oVR2:F;oVWC:O;oVWI:O;oVSO:O;oVRT:O;oVCT:O;
  //oVA:S;oVR1:F;oVR2:F;oVWC:C;oVWI:C;oVSO:C;oVRT:C;oVCT:C;
  //oVB:0;
  //oVR1:F;oVR2:F;oVB:1;
  //oVR1:R;oVR2:R;
  //oPW:1;
  //oPV:1;

  //oVA:S;

  //
  Configure_Valve("oVA", oVA);
  Configure_Valve("oVR1", oVR1);
  Configure_Valve("oVR2", oVR2);
  Configure_Valve("oVWC", oVWC);
  Configure_Valve("oVWI", oVWI);
  Configure_Valve("oVSO", oVSO);
  Configure_Valve("oVRT", oVRT);
  Configure_Valve("oVCT", oVCT);
}

void loop() {
  //Check for New Instructions and Read
  if (Serial.available()) {
    bool new_instructions = 1;
    EndConditionMet="F";
    iTS = millis();
    //std::map<std::string, std::vector<std::string>>
    instructions = ReadCommand(Serial.readStringUntil('\n').c_str());
  }

  //Update Time
  idT=millis()-iTS;

  //Basic Instruction read just executes the instruciton code
  if (instructions.at(IT)[0]=="PIB"){
     ActuateInstructions(instructions);
  }
 
  //Instruction Read Follows Safe State
  if (instructions.at(IT)[0]=="PI"){
    //Follow with stepped valve closing and opening
  }

  if (instructions.at(IT)[0]=="TR" or new_instructions = "1"){
    Serial.println(ReadSensors());
  }

  //Check Sensor Output
  CheckStopConditions();
//If reached end of Instructions, return to safe state
/*
  if (EndConditionMet=="F"){
    instructions == Safe_State;
  }
*/

  delay(20);
}
