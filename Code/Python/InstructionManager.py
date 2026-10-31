import os
import pandas as pd
import serial
import time
import pandas as pd

###Fetch Files
PathSISF = ".\\Wash_Instructions\\" #Relative Path for Wash Instructions
PathPMF = ".\\Process_Modifiers\\" #Relative Path for Process Modifiers
PathTL = ".\\Telemetry_Log\\" #Relative Path for Process Modifiers

SISF = "Default_Cycle.xlsx" #Selected Instruction Set File Name
PMF="Default_Modifiers.xlsx" #Selected Wash Cycle Modifiers

#DEBUG# print("Files:", os.listdir(PathSISF))
#DEBUG# os.listdir()

Instructions_df = pd.read_excel(os.path.join(PathSISF, SISF))
Modifiers = pd.read_excel(os.path.join(PathPMF, PMF)).set_index('abr')['val'].to_dict()
#print(Instructions_df)
#print(Modifiers)

def stripUnused(df,list):
    new_df=pd.DataFrame()
    for i in list:
        if i in df.columns:
            new_df[i] = df[i]
            #print("adding "+i)
    return new_df

###Read Instructions
#Instructions = pd.read_excel(os.path.join(PathSISF, SISF))

string="ehello"
MachineInstructionString= string.replace("he", "ai")

IULUI=['WSN','SSN','Action_Description'] #Utilized Instruciton List for UI
IULM=['oVCW','oVSW','oVWC','oVA','oVPR1','oVPR2','oVRT','oVCT','oPW','oPV','oPD','S1','S2','E1','E2'] #Utilized Instruciton List for Microcontroller

UII_df=stripUnused(Instructions_df,IULUI)
MI_df=stripUnused(Instructions_df,IULM)

def buildInstructionString(item):
    CommandString="IT:PI;"
    for name, value in item.items():
        CommandString=CommandString+(name+":"+str(value)+";")
    print(CommandString)
    '''
    for i in item:
        print(i[1])#+":"+i[1]+";")
        '''

df=MI_df
for Step in df.iterrows():
    #print(Step[1])
    buildInstructionString(Step[1])
    input("next?")
    #if serial available do telemetry request
    #parse
    #Build String
    #print instructions
    pass

#df.iterrows():

"""
def ParseTelemetry(telemetry):
    telemetry_dict = {}
    items = telemetry.split(";")
    for item in items:
        if ":" in item:
            key, value = item.split(":", 1)
            telemetry_dict[key] = value
    return telemetry_dict
#"""