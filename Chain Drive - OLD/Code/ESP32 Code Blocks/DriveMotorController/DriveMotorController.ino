/*
 * This ESP32 code is created by esp32io.com
 *
 * This ESP32 code is released in the public domain
 *
 * For more detail (instruction and wiring diagram), visit https://esp32io.com/tutorials/esp32-dc-motor
 */

#define PIN_IN1  19 // ESP32 pin GPIO19 connected to the IN1 pin L298
#define PIN_IN2  18 // ESP32 pin GPIO18 connected to the IN2 pin L298
#define PIN_ENA  21 // ESP32 pin GPIO17 connected to the EN1 pin L298

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pins as outputs.
  pinMode(PIN_IN1, OUTPUT);
  pinMode(PIN_IN2, OUTPUT);
  pinMode(PIN_ENA, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(PIN_IN1, HIGH); // control the motor's direction in clockwise
  digitalWrite(PIN_IN2, LOW);  // control the motor's direction in clockwise

  for (int speed = 0; speed <= 255; speed++) {
    analogWrite(PIN_ENA, speed); // speed up
    delay(10);
  }

  delay(2000); // rotate at maximum speed 2 seconds in clockwise direction
  // change direction
  

  delay(2000); // rotate at maximum speed for 2 seconds in anti-clockwise direction

  for (int speed = 255; speed >= 0; speed--) {
    analogWrite(PIN_ENA, speed); // speed down
    delay(10);
  }
  
  digitalWrite(PIN_IN1, LOW);   // control the motor's direction in anti-clockwise
  digitalWrite(PIN_IN2, HIGH);  // control the motor's direction in anti-clockwise
  delay(2000); // stop motor 2 second

    for (int speed = 0; speed <= 255; speed++) {
    analogWrite(PIN_ENA, speed); // speed up
    delay(10);
  }

  delay(2000); // rotate at maximum speed 2 seconds in clockwise direction
  // change direction

  for (int speed = 255; speed >= 0; speed--) {
    analogWrite(PIN_ENA, speed); // speed down
    delay(10);
  }

  delay(2000);
}
