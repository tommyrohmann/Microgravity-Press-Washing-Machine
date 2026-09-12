import os
from os import listdir
from os.path import isfile, join
import pandas as pd

import time
BootTime = float(time.time()/3600)

if __name__ == "__main__": #For Debug if I decide to run not as a module
    pass

class BootDataInter():
    @staticmethod
    def Read(Path):
        #Import and Format BootData
        BootDataFrame = pd.read_csv(Path) #Boot Data
        BD = pd.Series(BootDataFrame.Value.values, index=BootDataFrame.DataName).to_dict()
        for key in BD:
            try:
                BD[key]=float(BD[key])
            except:
                pass
            #print(key + str(type(BD[key])))
        return BD
    
    @staticmethod
    def Write(BootData,Path):
        BootDataFrame = pd.DataFrame(list(BootData.items()), columns=["DataName", "Value"])
        BootDataFrame.to_csv(Path, index=False)

class CycleConfigInter():
    @staticmethod
    def GetOptions(path):
        return [f for f in listdir(path) if isfile(join(path, f))]
    
    @staticmethod
    def ReadSelection(file):
        try: instructions = pd.read_excel(file)
        except: instructions = pd.read_csv(file)
        return instructions

"""
    '''
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
'''
    @staticmethod
    def RecordWashData(path,FileName,data): ###NEED TO CONFIGURE AS FUNCTION. DOES NOT WORK
        pass
    '''
        WashCount = str(random.randint(1,100))+".csv" #stand in for tracker
        FileName = os.path.join(path,WashCount)
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
#'''
#"""