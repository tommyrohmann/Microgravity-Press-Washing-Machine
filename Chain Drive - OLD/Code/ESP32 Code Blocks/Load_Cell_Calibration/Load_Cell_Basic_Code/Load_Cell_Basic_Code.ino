#include "HX711.h"
HX711 scale;

uint8_t dataPin = 22;
uint8_t clockPin = 23;

uint32_t start, stop;
volatile float f;
float scaleMultFactor = 4050;
float calibrationWeight = 1;

void setup() {
  Serial.begin(115200);
  
  //Scale Setup
  scale.begin(dataPin, clockPin); //treating pins as scale/reading as such
  scale.set_scale(scaleMultFactor);
  scale.tare();
}

void loop()
{
  Serial.println(scale.get_units(5));
  Serial.println(scaleMultFactor);
  delay(10);
}
