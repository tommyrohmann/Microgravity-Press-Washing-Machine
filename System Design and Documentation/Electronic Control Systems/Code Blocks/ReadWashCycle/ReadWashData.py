import time
from csv import DictReader

with open("Sample_Wash_Cycle.csv", 'r') as f:
    dict_reader = DictReader(f)
    list_of_dict = list(dict_reader)

Current_Phase = 'NULL'
Current_Action = 'NULL'
Process_Length = 'NULL'
Process_Progress = 'NULL'

while True:
    for i in range(len(list_of_dict)):
        
        current = list_of_dict[i]

        #Packing Items for TX
        TX = [
            int(current['VA_WWI']),
            current['VA_WWO'],
            current['VA_XO'],
            current['VA_A'],
            current['VB'],
            current['DM_DIR_WASH'],
            current['DM_SPD_WASH'],
            current['DM_DIR_RES'],
            current['DM_SPD_RES'],
            current['P_DD'],
            current['NST1_i'],
            current['NST1_r'],
            current['NST1_v'],
            current['NST2_i'],
            current['NST2_r'],
            current['NST2_v'],
        ]

        #display items for GUI
        Process_Length = len(list_of_dict)
        Process_Progress = (f"{i+1}/{Process_Length}")
        if current['WSN'] != '':
            Current_Phase = current['WSN']
        if current['SSN'] != '':
            Current_Action = current['SSN']
        print(f"Progress:{Process_Progress} | {Current_Phase} | {Current_Action} \n {TX}")

        #package = (",".join(current.values()))
        #print(package)
        time.sleep(1)
    break
