import pandas as pd
import random
import os

WashDataDir = "WashData"
WashCount = str(random.randint(1,100))+".csv" #stand in for tracker
FileName = os.path.join(WashDataDir,WashCount)
print(FileName)

WashData = {'WPS': 'nan', 'P_Res': 'PSI', 'P_Wash': 'PSI', 'LC_Wash_1': 'lbf', 'LC_Wash_2': 'lbf', 'LC_Res_1': 'lbf', 'LC_Res_2': 'lbf', 'NF_W': 'lbf', 'NF_R': 'lbf', 'DR_W': 'lbf', 'DF_R': 'lbf', 'CS_VV': 'amps', 'CS_WS': 'amps', 'RE_Wash': 'in', 'RE_Res': 'in', 'LS_RFR': 'bool', 'LS_PTC': 'bool', 'LS_WFE': 'bool', 'E_Stop': 'bool', 'LS_WC': 'bool', 'ET': 'ms', 'TET': 'ms'}
for key, value in WashData.items():
        WashData[key]=float('nan')

WashDataFrame = pd.DataFrame([WashData])
WashDataFrame.to_csv(FileName, mode='a', index=False, header=True)

done = 0 #unimportant
while done < 5:
    #simulate reading data from serial
    for key, value in WashData.items():
        WashData[key] = random.randint(1,10)
        #print(key,value)
    print(WashData)
    WashDataFrame = pd.DataFrame([WashData])
    WashDataFrame.to_csv(FileName, mode='a', index=False, header=False)

    done += 1