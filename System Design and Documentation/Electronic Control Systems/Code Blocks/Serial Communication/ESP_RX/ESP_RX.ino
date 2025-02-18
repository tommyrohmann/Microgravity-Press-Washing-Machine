void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // Wait for serial port to connect
  }
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    String receivedData = Serial.readStringUntil('\n');
    String data = "Hello:World";
  int index = data.indexOf(':'); // Find the position of the colon

  if (index != -1) {
    String part1 = data.substring(0, index);      // Substring before the colon
    String part2 = data.substring(index + 1);    // Substring after the colon
    
    Serial.println(part1); // Output: Hello
    Serial.println(part2); // Output: World
  }
    Serial.println(receivedData);
  }
}