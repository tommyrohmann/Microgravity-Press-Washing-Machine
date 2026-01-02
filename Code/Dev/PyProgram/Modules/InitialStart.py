if __name__ =="__main__":
    from MachineFunctions import BootDataInter
    from MachineFunctions import CycleConfigInter
else:
    from Modules.MachineFunctions import BootDataInter
    from Modules.MachineFunctions import CycleConfigInter
import time as time

class Config():
    WashCycleDir = ".\ProcessFiles\WashInstructions" #Location of Wash Instructions for Selection
    ProcessModifierDir = ".\ProcessFiles\WashInstructions\ProcessModifiers" #Process Modifier
    BootDataFilePath = ".\Config\BootData.csv"

    #GetPathData
    BootData = BootDataInter.Read(BootDataFilePath)
    CycleOptions = CycleConfigInter.GetOptions(WashCycleDir)
    ModifierOptions = CycleConfigInter.GetOptions(ProcessModifierDir)

    CycleSelection = {"Cycle":BootData["DefaultWashProcess"],#set selection to default,
                    "Modifier":BootData["DefaultWashModifier"],
                }
    
    #print(CycleSelection)

###Wash Instruction
class Wash():
    I=CycleConfigInter.ReadSelection(f'{Config.WashCycleDir}\{Config.CycleSelection["Cycle"]}')#Need to get full path
    #I=I.to_dict()

#time.sleep(5) #Simulate Process Execution and Update Post Process
BootTime = float(time.time()/3600)
Config.BootData["RunHours"] = float(Config.BootData["RunHours"])
Config.BootData["RunHours"] += float(time.time()/3600) - BootTime #Add Process Time to Total Recorded Run Time
Config.BootData["WashCount"] = int(Config.BootData["WashCount"]+1)

print(Wash.I)
#print(Config.CycleSelection)