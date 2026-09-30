int pushButton1 = 35;
int pushButton2 = 32;
int PWash = 34;
int PComp = 76;

int rLED = 25;
int yLED = 33;
int gLED1 = 26;
int gLED2 = 27;

double TET = 0; //total elapsed time since process start
double ET = 0; //Elapsed Time of Process


void setup() {
  Serial.begin(9600);
  while (!Serial) {
    delay(10);
  }

  pinMode(rLED, OUTPUT);
  pinMode(yLED, OUTPUT);
  pinMode(gLED1, OUTPUT);
  pinMode(gLED2, OUTPUT);

  pinMode(pushButton1, INPUT);
  pinMode(pushButton2, INPUT);
}

//dictionary of sorts
struct Item {
  String key;
  String value;
};

Item items[30];
int itemCount = 0;
String command;
String complete = "f";

void parseMessage(String msg) {
  itemCount = 0;
  command = "";

  int start = 0;

  while (true) {
    int end = msg.indexOf(';', start);
    if (end == -1) break;

    String token = msg.substring(start, end);
    start = end + 1;

    if (token.length() == 0) continue;

    // First token is command (no colon)
    if (token.indexOf(':') == -1) {
      command = token;
      continue;
    }

    // Parse key:value
    int colon = token.indexOf(':');
    if (colon == -1) continue;

    items[itemCount].key = token.substring(0, colon);
    items[itemCount].value = token.substring(colon + 1);
    itemCount++;
  }
}

String getValue(String key) {
  for (int i = 0; i < itemCount; i++) {
    if (items[i].key == key)
      return items[i].value;
  }
  return "";
}

void loop() {
  if (Serial.available()) {
    String incoming = Serial.readStringUntil('\n');
    parseMessage(incoming); //parse message
  }

  if(command == "WI") {
    //Serial.print(complete + ";");
    //set pinstates and stop conditions
    digitalWrite(rLED, getValue("L1").toInt());
    digitalWrite(yLED, getValue("L2").toInt());
    digitalWrite(gLED1, getValue("L3").toInt());
    digitalWrite(gLED2, getValue("L4").toInt());
    complete = "f";
  }

  if(command == "TR"){
    Serial.print("L:" + complete + ";");
    Serial.print(String("II:")+String("nan")+";");
    Serial.print("TET:"+String(millis())+";");
    Serial.print("PR:"+String(analogRead(Ptrans))+";");
    Serial.println("");
    /*
    //Serial.print(command + ";");
    Serial.print("L1:" + getValue("L1") + ";");
    Serial.print("L2:" + getValue("L2") + ";");
    Serial.print("L3:" + getValue("L3") + ";");
    Serial.print("L4:" + getValue("L4") + ";");
    Serial.print("S1:" + getValue("S1") + ";");  // "2,=,HIGH"
    Serial.print("\n");
    */
  }

  if (digitalRead(pushButton1) == HIGH){
    complete = "t";
  }
  //WI;L1:0;L2:0;L4:1;L3:0;S1:1,=,HIGH;
  //if stop conditions met, complete = t
  command = "NA";
}
