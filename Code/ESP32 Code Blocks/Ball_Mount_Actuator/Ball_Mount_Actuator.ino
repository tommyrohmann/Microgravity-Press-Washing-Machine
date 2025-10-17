#include <ESP32Servo.h>  // Include the ESP32Servo library
/*
VA_WWI,
2,Washwater Outlet Valve Actuator,VA_WWO,
3,Cross-over Valve Actuator,VA_XO,
4,Air Valve Actuator,VA_A,
5,Wash Piston Drive Motor,DM_Wash,
6,Reservoir Piston Drive Motor,DM_Res,
7,DetergentDosing,DD,
*/
int vAWWI = 26;
int VA_WWO = 25;
int VA_XO = 33;
int VA_A = 32;

Servo vAWWI;

void setup() {
  Serial.begin(115200);
  vAWWI.setPeriodHertz(50);
  vAWWI.attach(servoPin, 400, 2400);
}

void loop() {
  vAWWI.write(35);  // Set the servo to the current angle
  delay(500);  // Wait for the servo to reach the position
  vAWWI.write(135);  // Set the servo to the current angle
  delay(1000);  // Wait for the servo to reach the position
}
