import os
from os import listdir
from os.path import isfile, join

def LoadWashInstructionOptions(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

Options = LoadWashInstructionOptions("WashInstructions")

index = int(input("Which wash cycle?"))
WashCycle = Options[index]
print(WashCycle)