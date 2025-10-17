import os
from os import listdir
from os.path import isfile, join
import pandas as pd

#File Paths
WashCycleDir = "WashInstructions" #Location of Wash Instructions for Selection
    #Safety Stop File
    #Safe State Default
    #Prewash File Location
    
    #Instruction Abbreviation Save
    #Data Log Folder
StateFile = "4" #Save of Run Time, Default Cycle, and Wash Count

#Initialization

#Select Wash Cycle
Options = [f for f in listdir(WashCycleDir) if isfile(join(WashCycleDir, f))]

index = int(input("Which wash cycle?"))
WashCycle = Options[index]
print(join(WashCycleDir, WashCycle))
print(listdir())

#Read Wash Cycle
WashInstructions = pd.read_csv(WashCycle)
print(WashCycle)