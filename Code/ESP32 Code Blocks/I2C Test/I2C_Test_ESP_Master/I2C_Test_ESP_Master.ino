#include <Wire.h>

#define SLAVE_ADDRESS 0x08  // Address of the Arduino Slave

void setup() {
    Serial.begin(115200);
    Wire.begin(21, 22);  // Initialize I2C with SDA on GPIO 21 and SCL on GPIO 22
}

void loop() {
    Wire.requestFrom(SLAVE_ADDRESS, 4);  // Request 4 bytes from the Arduino

    if (Wire.available() == 4) {
        int value1 = (Wire.read() << 8) | Wire.read();  // Reconstruct first integer
        int value2 = (Wire.read() << 8) | Wire.read();  // Reconstruct second integer
        Serial.print("Received: ");
        Serial.print(value1);
        Serial.print(", ");
        Serial.println(value2);
    } else {
        Serial.println("Error: Incorrect byte count received.");
    }

    delay(10);  // Request data every second
}
