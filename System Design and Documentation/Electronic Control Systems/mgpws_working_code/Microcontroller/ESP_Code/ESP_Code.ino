#include <ESP32Servo.h>  // Include the ESP32Servo library

/*
1,Washwater Inlet Valve Actuator,VA_WWI;
2,Washwater Outlet Valve Actuator,VA_WWO;
3,Cross-over Valve Actuator,VA_XO;
4,Air Valve Actuator,VA_A;
5,ValveActuatorMastSwitch,VAMS;
6,Wash Piston Drive Motor,DM_Wash;
7,Reservoir Piston Drive Motor,DM_Res;
8,DetergentDosingPump,P_DD;
*/

/*
1,
2,
3,
4,
5,
6,

*/

//The lines below define the pin numbers for each 
//Actuators
const int VA_WWI_Pin = 26;  // Pin connected to the servo
const int VA_WWO_Pin = 25;
const int VA_XO_Pin = 33;
const int VA_A_Pin = 32;
const int VAMS_Pin = 0;
const int DM_Wash_FWD_Pin = 0;
const int DM_Wash_FWD_Rev = 0;
const int DM_Res_FWD_Pin = 0;
const int DM_Res_Rev_Pin = 0;
const int P_DD = 0;

//Sensors
const int 
const int

//Interpereted Sensor Values


//Make Servo Objects
Servo VA_WWI;
Servo VA_WWO;
Servo VA_XO;
Servo VA_A;



void setup() {
  Serial.begin(115200);
  
  // Attach the servo to the correct pin with a range for the pulse width
  VA_WWI.setPeriodHertz(50);  // Set the servo PWM frequency to 50Hz
  VA_WWI.attach(VA_WWI_Pin, 400, 2400);

  VA_WWO.setPeriodHertz(50);
  VA_WWO.attach(VA_WWO_Pin, 400, 2400);

  VA_XO.setPeriodHertz(50);
  VA_XO.attach(VA_XO_Pin, 400, 2400);

  VA_A.setPeriodHertz(50);
  VA_A.attach(VA_A_Pin, 400, 2400);  // Attach the servo to pin 26, set pulse width range
}

void loop() {
  VA_WWI.write(35);
  VA_WWO.write(35);
  VA_XO.write(35);
  VA_A.write(35);
  delay(5000);  // Wait for the servo to reach the position
  
  VA_WWI.write(135);
  VA_WWO.write(135);
  VA_XO.write(135);
  VA_A.write(135);
  delay(5000);  // Wait for the servo to reach the position
}
