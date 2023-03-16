#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(9);
  Serial.begin(9600);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  while (1==1) {
        myservo.write(0);              // tell servo to go to position in variable 'pos'
    delay(10);
    myservo.write(90);
    delay(10);
    Serial.print(1);
  }
}

