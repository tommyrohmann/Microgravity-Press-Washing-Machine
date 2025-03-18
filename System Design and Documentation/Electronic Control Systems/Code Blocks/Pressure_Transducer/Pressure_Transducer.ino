#include <Wire.h>

#define NANO_I2C_ADDRESS 0x08 // Address for the ESP32 to request data

void setup() {
    Wire.begin(NANO_I2C_ADDRESS);  // Initialize as I2C slave
    Wire.onRequest(sendData);      // Register function to send data when requested
}

void loop() {
    // Nothing needed in loop
}

void sendData() {
    int value1 = 123;
    int value2 = 456;

    Wire.write((uint8_t)(value1 >> 8));  // High byte of value1
    Wire.write((uint8_t)(value1 & 0xFF)); // Low byte of value1
    Wire.write((uint8_t)(value2 >> 8));  // High byte of value2
    Wire.write((uint8_t)(value2 & 0xFF)); // Low byte of value2
}
