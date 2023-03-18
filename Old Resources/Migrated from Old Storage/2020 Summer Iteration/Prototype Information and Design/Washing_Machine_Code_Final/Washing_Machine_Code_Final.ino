int WashState = 0;
const int LARetract = 2;
const int LAExtend = 3;
const int BypassSolenoid = 4;
const int AirSolenoid = 5;
const int DirtyWaterSolenoid = 6;
const int CleanWaterSolenoid = 7;
const int NextStateTrigger = 13;
const int PrevStateTrigger = 12;
const int FirstStateEStop = 11;
const int AmperageSensor = A1;


void setup() {
  pinMode(NextStateTrigger, INPUT);
  pinMode(PrevStateTrigger, INPUT);
  pinMode(FirstStateEStop, INPUT);
  pinMode(AmperageSensor, INPUT);
  pinMode(LARetract, OUTPUT);
  pinMode(LAExtend, OUTPUT);
  pinMode(BypassSolenoid, OUTPUT);
  pinMode(AirSolenoid, OUTPUT);
  pinMode(DirtyWaterSolenoid, OUTPUT);
  pinMode(CleanWaterSolenoid, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  //State Triggers {
  if (digitalRead(NextStateTrigger) == HIGH) {
    while (digitalRead(NextStateTrigger) == HIGH) {
      delay (1);
    }
    WashState = WashState + 1;
    if ((WashState) == 8) {
      WashState = 0;
    }
    Serial.print(WashState);
  }
  if (digitalRead(PrevStateTrigger) == HIGH) {
    while (digitalRead(PrevStateTrigger) == HIGH) {
      delay (1);
    }
    WashState = WashState - 1;
    if ((WashState) == -1) {
      WashState = 7;
    }
    Serial.print(WashState);
  }
  if (digitalRead(FirstStateEStop) == HIGH) {
    while (digitalRead(FirstStateEStop) == HIGH) {
      delay (1);
    }
    WashState = 0;
    Serial.print(WashState);
  }

  // } State Triggers



  // States {

  if (WashState == 0) {
    //Resting State. Default to here for E-Stop.
    digitalWrite(LARetract, LOW);
    digitalWrite(LAExtend, LOW);
    digitalWrite(BypassSolenoid, LOW);
    digitalWrite(AirSolenoid, LOW);
    digitalWrite(DirtyWaterSolenoid, LOW);
    digitalWrite(CleanWaterSolenoid, LOW);
  }
  if (WashState == 1) {
    //Pre-Wash-Process Retraction. Primes Washing Machine for use and reduces chances of physical issues.
    digitalWrite(LARetract, HIGH);
    digitalWrite(LAExtend, LOW);
    digitalWrite(BypassSolenoid, HIGH);
    digitalWrite(AirSolenoid, HIGH);
    digitalWrite(DirtyWaterSolenoid, LOW);
    digitalWrite(CleanWaterSolenoid, LOW);
  }
  if (WashState == 2) {
    //Soaking Phase 1: NO SAFETY ON THIS PHASE AMPERAGE SENSOR NOT IN USE. Pressing shirt to displace air in Wash Chamber.
    digitalWrite(LARetract, LOW);
    digitalWrite(LAExtend, HIGH);
    digitalWrite(BypassSolenoid, HIGH);
    digitalWrite(AirSolenoid, LOW);
    digitalWrite(DirtyWaterSolenoid, LOW);
    digitalWrite(CleanWaterSolenoid, LOW);
  }
  if (WashState == 3) {
    //Soaking Phase 2: Drawing water from Clean Water Solenoid to wet shirt while expelling air.
    digitalWrite(LARetract, HIGH);
    digitalWrite(LAExtend, LOW);
    digitalWrite(BypassSolenoid, LOW);
    digitalWrite(AirSolenoid, HIGH);
    digitalWrite(DirtyWaterSolenoid, LOW);
    digitalWrite(CleanWaterSolenoid, HIGH);
  }
  if (WashState == 4) {
    //Agitation Phase 1: NO SAFETY ON THIS PHASE AMPERAGE SENSOR NOT IN USE. Compress shirt to generate flow.
    digitalWrite(LARetract, LOW);
    digitalWrite(LAExtend, HIGH);
    digitalWrite(BypassSolenoid, HIGH);
    digitalWrite(AirSolenoid, LOW);
    digitalWrite(DirtyWaterSolenoid, LOW);
    digitalWrite(CleanWaterSolenoid, LOW);
  }
  if (WashState == 5) {
    //Agitation Phase 2: Decompress shirt to generate flow.
    digitalWrite(LARetract, HIGH);
    digitalWrite(LAExtend, LOW);
    digitalWrite(BypassSolenoid, HIGH);
    digitalWrite(AirSolenoid, LOW);
    digitalWrite(DirtyWaterSolenoid, LOW);
    digitalWrite(CleanWaterSolenoid, LOW);
  }
  if (WashState == 6) {
    //Dry Phase 1: NO SAFETY ON THIS PHASE AMPERAGE SENSOR NOT IN USE. Compress shirt and intake air while expelling water.
    digitalWrite(LARetract, LOW);
    digitalWrite(LAExtend, HIGH);
    digitalWrite(BypassSolenoid, LOW);
    digitalWrite(AirSolenoid, HIGH);
    digitalWrite(DirtyWaterSolenoid, HIGH);
    digitalWrite(CleanWaterSolenoid, LOW);
  }
  if (WashState == 7) {
    //Dry Phase 2: Decompressing shirt filling wash chamber with air.
    digitalWrite(LARetract, HIGH);
    digitalWrite(LAExtend, LOW);
    digitalWrite(BypassSolenoid, HIGH);
    digitalWrite(AirSolenoid, HIGH);
    digitalWrite(DirtyWaterSolenoid, LOW);
    digitalWrite(CleanWaterSolenoid, LOW);
  }
  
  // } States
}
