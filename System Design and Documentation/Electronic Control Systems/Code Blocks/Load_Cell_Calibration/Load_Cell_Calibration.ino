#define ENCODER1_A 2 // Pin for Encoder 1 A phase (Interrupt 0)
#define ENCODER1_B 8 // Pin for Encoder 1 B phase
#define ENCODER2_A 3 // Pin for Encoder 2 A phase (Interrupt 5)
#define ENCODER2_B 9 // Pin for Encoder 2 B phase

volatile long encoder1Count = 0; // Extended counter for Encoder 1
volatile long encoder2Count = 0; // Extended counter for Encoder 2
volatile bool encoder1Direction = true; // True = CW, False = CCW
volatile bool encoder2Direction = true; // True = CW, False = CCW

void handleEncoder1() {
  bool aState = digitalRead(ENCODER1_A);
  bool bState = digitalRead(ENCODER1_B);
  encoder1Direction = (aState != bState); // CW if A != B
  encoder1Count += encoder1Direction ? 1 : -1;
}

void handleEncoder2() {
  bool aState = digitalRead(ENCODER2_A);
  bool bState = digitalRead(ENCODER2_B);
  encoder2Direction = (aState != bState); // CW if A != B
  encoder2Count += encoder2Direction ? 1 : -1;
}

void setup() {
  Serial.begin(115200);

  // Setup pins as input
  pinMode(ENCODER1_A, INPUT_PULLUP);
  pinMode(ENCODER1_B, INPUT_PULLUP);
  pinMode(ENCODER2_A, INPUT_PULLUP);
  pinMode(ENCODER2_B, INPUT_PULLUP);

  // Attach interrupts
  attachInterrupt(digitalPinToInterrupt(ENCODER1_A), handleEncoder1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENCODER2_A), handleEncoder2, CHANGE);
}

void loop() {
  // Print encoder counts and directions
  static long lastEncoder1Count = 0;
  static long lastEncoder2Count = 0;

  if (encoder1Count != lastEncoder1Count) {
    Serial.print("Encoder 1 Count: ");
    Serial.println(encoder1Count);
    Serial.print("Encoder 1 Direction: ");
    Serial.println(encoder1Direction ? "CW" : "CCW");
    lastEncoder1Count = encoder1Count;
  }

  if (encoder2Count != lastEncoder2Count) {
    Serial.print("Encoder 2 Count: ");
    Serial.println(encoder2Count);
    Serial.print("Encoder 2 Direction: ");
    Serial.println(encoder2Direction ? "CW" : "CCW");
    lastEncoder2Count = encoder2Count;
  }

  delay(50); // Adjust delay as necessary
}