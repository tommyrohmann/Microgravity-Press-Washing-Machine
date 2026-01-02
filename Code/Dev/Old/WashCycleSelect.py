import os
from os import listdir
from os.path import isfile, join
import pandas as pd

#WashCyclePaths
WashCycleDir = "WashInstructions" #Location of Wash Instructions for Selection
ProcessModifierDir = "WashInstructions\ProcessModifiers" #Process Modifier


#Initialization


#~~~~~~~~~~~~USER INTERFACE/PROCESS SELECTION~~~~~~~~~~~~~~~~
#Select Wash Cycle
Options = [f for f in listdir(WashCycleDir) if isfile(join(WashCycleDir, f))]
print(Options)
UserSelection = int(input("Which wash cycle?"))
WashCycleSelect = Options[UserSelection]
WashCycleSelect = os.path.join(WashCycleDir, WashCycleSelect)

#Select Wash Modifier
Options = [f for f in listdir(ProcessModifierDir) if isfile(join(ProcessModifierDir, f))]
print(Options)
UserSelection = int(input("Which wash mode?"))
ModifierSelect = Options[UserSelection]
ModifierSelect = os.path.join(ProcessModifierDir, ModifierSelect)

#~~~~~~~~~~~~~~~~Read Wash Cycle~~~~~~~~~~~~~~~~~~~~~~
try: WashModifiers = pd.read_excel(ModifierSelect)
except:
    WashModifiers = pd.read_csv(ModifierSelect)
WashModifiers = pd.Series(WashModifiers.Value.values, index=WashModifiers.Modifier).to_dict()
print(WashModifiers)

try: WashInstructions = pd.read_excel(WashCycleSelect)
except: WashInstructions = pd.read_csv(WashCycleSelect)
print(WashCycleSelect)

print(WashInstructions)


"""
#~~~~~~~~~~~Run Wash Cycle~~~~~~~~~~~~~~~
for i, row in WashInstructions.iterrows():
    PhaseDone = 0 #
    a=WashInstructions.iloc[i] #Get current wash direction
    ConfigureValves = #Make For Loop that will read if an instruction is a valve or not.
    DisplacementAction = {
        #Everything else is what it was for configure valves
        #
    }
        #Package data to send to Microcontroller - turns from dictionary to format readable by arduino/esp32
        #Send data to microcontroller

        #DataRead Loop, terminates when arduino says its done
    for substep in [ConfigureValves,DisplacementAction]
    while(PhaseDone == 0):
        #Configure Valves

        #Displacement Action



print(WashInstructions)


#'''
#"""