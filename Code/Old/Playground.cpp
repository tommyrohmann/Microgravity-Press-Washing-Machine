#include <iostream>
#include <map>
#include <string>
#include <variant>
#include <vector>

std::map<std::string, double> SensorStates{
  {"iPT1",0},
  {"iPT2",0}, //
  {"iT",0}, //microcontroller time
  {"iTd",0}, //Instruction dT
  {"iTS",0}, //Start of Instruction
  {"iES",0}, //EMCY STOP
  {"ECM",1}, //End Condition Met
};

int main(){
    std::string telemetry = "";
    for (auto const& [key, val] : SensorStates){
        telemetry += key + ":" + std::to_string(val) + ";";
    }

    std::cout << telemetry;
    //std::cout>>telemetry;

    //std::cout << SensorStates["iPT1"];

}
