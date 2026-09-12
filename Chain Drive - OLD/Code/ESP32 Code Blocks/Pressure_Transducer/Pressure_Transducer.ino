// Define the analog pin you want to read fromAdd commentMore actions
const int analogPin = 34;  // You can change this to any other valid analog pin on your ESP32

void setup() {
  // Start the serial communication to send the data to the Serial Monitor
  Serial.begin(115200);
  // Wait for the serial port to open
  while (!Serial);
  Serial.println("ESP32 Analog Read Example");
}

void loop() {
  // Read the value from the analog pin (values between 0 and 4095 for ESP32)
  int analogValue = analogRead(analogPin);

  // Print the analog value to the Serial Monitor
  Serial.print("Analog value: ");
  Serial.println(analogValue);

  // Wait for a short time before the next reading (in milliseconds)
  delay(1000);
}