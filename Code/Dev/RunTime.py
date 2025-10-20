import time
import pandas as pd

BootDataFilePath = "BootData.csv" #BootData Time

#Get Boot Time
BootTime = float(time.time()/3600)

#Import and Format BootData
BootDataFrame = pd.read_csv(BootDataFilePath) #Boot Data
BD = pd.Series(BootDataFrame.Value.values, index=BootDataFrame.DataName).to_dict()
for key, value in BD.items():
    try:
        BD[key]=float(BD[key])
    except:
        pass

#Run Process
time.sleep(5) #Simulate Process Execution and Update Post Process
BD["RunHours"] += float(time.time()/3600) - BootTime #Add Process Time to Total Recorded Run Time
BD["WashCount"] = int(BD["WashCount"]+1)

BootDataFrame = pd.DataFrame(list(BD.items()), columns=["DataName", "Value"])
BootDataFrame.to_csv(BootDataFilePath, index=False)

#Check
BootDataFrame1 = pd.read_csv(BootDataFilePath)
print("\nRe-read DataFrame:\n", BootDataFrame1)