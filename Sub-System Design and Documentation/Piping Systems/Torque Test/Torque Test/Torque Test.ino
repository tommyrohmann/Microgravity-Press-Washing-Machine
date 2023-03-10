//
//    FILE: HX_kitchen_scale.ino
//  AUTHOR: Rob Tillaart
// VERSION: 0.1.0
// PURPOSE: HX711 demo
//     URL: https://github.com/RobTillaart/HX711
//
// HISTORY:
// 0.1.0    2020-06-16 initial version
//

// to be tested 

#include "HX711.h"

HX711 scale;

uint8_t dataPin = 6;
uint8_t clockPin = 7;

float w1, w2, previous = 0;

void setup()
{
  Serial.begin(115200);
  Serial.println(__FILE__);
  Serial.print("LIBRARY VERSION: ");
  Serial.println(HX711_LIB_VERSION);
  Serial.println();

  scale.begin(dataPin, clockPin);

  Serial.print("UNITS: ");
  Serial.println(scale.get_units(10));

  // loadcell factor 20 KG
  // scale.set_scale(127.15);
  // loadcell factor 5 KG
  scale.set_scale(3972.86962);
  scale.tare();

  Serial.print("UNITS: ");
  Serial.println(scale.get_units(10));
}

void loop()
{
  // read until stable
  w1 = scale.get_units(10);
    Serial.println(w1);

}

// END OF FILE
