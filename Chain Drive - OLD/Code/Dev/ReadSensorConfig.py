import pandas as pd
SensorListDir = "Config\SensorList.xlsx"
SensorInfo = pd.read_excel(SensorListDir)
print(SensorInfo)

a = SensorInfo.set_index('Sensor_Label')['Units'].to_dict()

#print(a)
#print (a.keys())

b=""

#Build Readout String
for key in a.keys():
    b = b + str(key).strip() + ":" + str(a[key]).strip() + ", "
    #b = b + str(a[value]).strip("'") + ","
    
    #b[key]=str(value).strip()
print(b)
'''
Instruction = {
        "Valve":"",
        "ResPiston":"",
        "WashPiston":"",
        "Stop1":"",
        "Stop2":""
    }
'''
#Build Data Transfer String
for i,j in a.items():
    print(i) #Variable
    print(j) #Package Group
#""""""