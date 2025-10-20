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
print(Options)
index = int(input("Which wash cycle?"))
WashCycleSelect = Options[index]
WashCycleSelect = os.path.join(WashCycleDir, WashCycleSelect)
#print(listdir())

print(WashCycleSelect)

#Read Wash Cycle
WashInstructions = pd.read_csv(WashCycleSelect)
#print(WashInstructions.to_string())
#"""
#Run Wash Cycle
for i, row in WashInstructions.iterrows():
    a=WashInstructions.iloc[i]
    print(a["SSN"])
    #print(f"Index: {index}, WSN: {row['WSN']}, SSN: {row['SSN']}")

"""
a = WashInstructions.iloc[2]
print(a["3"])
#print(WashInstructions.iloc[2]["3"])
"""