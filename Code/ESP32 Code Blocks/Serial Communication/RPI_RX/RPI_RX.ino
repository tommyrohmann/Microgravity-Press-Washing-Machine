void setup() {
  // Start the serial communication at 115200 baud rate
  Serial.begin(115200);

  // Wait for the serial port to connect (optional, mostly for boards with native USB like ESP32)
  while (!Serial) {
    delay(10);
  }
  Serial.println("ESP32 Serial Monitor Ready!");
}

void loop() {
  // Check if data is available in the serial buffer
  if (Serial.available()) {
    // Read the incoming data as a string
    String incomingData = Serial.readStringUntil('\n'); // Reads until a newline character
    Serial.println("Received: " + incomingData);      // Print the received data
  }
}
