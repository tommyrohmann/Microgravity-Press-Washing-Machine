import pandas as pd

Terminate_Process = 0
WashSelection = "WashInstructions\Default_Wash_Cycle.xlsx"
BlankInstructionDir = "WashInstructions\ProcessRun\SafeState.xlsx"
BlankInstruction = pd.read_excel(BlankInstructionDir)

WashInstructions = pd.read_excel(WashSelection)
print(len(WashInstructions))

for index, row in WashInstructions.iterrows():
    #Configure

    ####Python Break up Phase to substeps
    for i in ["Close_VVs","Open_VVs","Displacement"]:
        if i == "Close_VVs":
            print(row["WSN"])
        if i == "Open_VVs":
            pass
        if i == "Displacement":
            print("")

        #####Package Instructions

        #####Send Instruction

        ####Wait for Response Loop
            #Wait Set Time
            #Send Ready to RX Command
            #if serial available
                #recieve and interperet RX Data. append to wash record file
                #if complete == true, break and go to next instance of for loop

    
    if Terminate_Process == 1:
        break