import serial
import time
import pandas as pd

print("hi")

###Telemetry Log Setup
TelemetryLog = pd.DataFrame()
TelemetryLogName = "TelemetryLog" + time.strftime("%Y%m%d-%H%M%S")+".xlsx"

###Package Label Key Readout
PackageLabelKey = pd.read_excel('PackageLabelKey.xlsx')
PackageLabelKey = PackageLabelKey.set_index('Device_Name')['Package_Label'].to_dict()
ConsolidationKey = pd.read_excel('PackageLabelKey.xlsx').set_index('Device_Name')['Used_By_Controller'].to_dict()
ContainerLabelKey = pd.read_excel('PackageLabelKey.xlsx').set_index('Device_Name')['Contains'].to_dict()

###Read Instructions
Instructions = pd.read_excel('instructions.xlsx')

###Replace Variable in DataFrame with Variable Values
Modifiers = pd.read_excel('Modifiers.xlsx').set_index('Modifier')['Value'].to_dict()
for i in Modifiers:
    pass
    Instructions.replace(i, Modifiers[i], inplace=True)

###Consolidate Multi-Instruction Data into Single Columns as Specified in Package Label Key
AddPackets = [c for c in ContainerLabelKey.keys() if c not in Instructions.columns] #Identify what isnt a data packet/not in instructions, add data packets to list
for packet in AddPackets: #for each packet that needs to be added to instructions
    PacketContent = ContainerLabelKey[packet].split(',')
    Instructions[packet] = Instructions[PacketContent].astype(str).agg(",".join, axis=1)

###Prepare Data for Packaging
#Strip Unused Columns for packaging
for key in ConsolidationKey.keys(): #Rename new columns to their container labels
    if ConsolidationKey[key] == 'n':
        print("NaN Detected, skipping...")
        del Instructions[key]
print(Instructions)


### Set up the serial connection
ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with your Arduino's port
time.sleep(2)  # Wait for the connection to initialize

### Clear the serial buffers to avoid residual data
ser.reset_input_buffer()
ser.reset_output_buffer()
ser.read_all()

def ParseTelemetry(telemetry):
    telemetry_dict = {}
    items = telemetry.split(";")
    for item in items:
        if ":" in item:
            key, value = item.split(":", 1)
            telemetry_dict[key] = value
    return telemetry_dict

#Build Readout String
for i, row in Instructions.iterrows():
    package = "IT:1;" #initiate start of instruciton package

    for item in Instructions.columns:
        package += PackageLabelKey[item] + ":" + str(row[item]).strip() + ";"

    print("sent: " + package)
    ser.write(package.encode() + b'\n')
    complete = False
    while(complete == False):
        ser.write("IT:1;".encode() + b'\n')
        response = ser.readline().decode("utf-8", errors="ignore").strip()
        #print("Received from Arduino:", response)
        time.sleep(.125)
        ReadTelemetry = ParseTelemetry(response)
        print(ReadTelemetry)
        
        if ReadTelemetry['L'] == "t":
            complete = True

        if TelemetryLog.empty:
            TelemetryLog = pd.DataFrame(columns=ReadTelemetry.keys())
            '''for key in ReadTelemetry.keys():
                TelemetryLog[key] = []'''
        TelemetryLog.loc[len(TelemetryLog)] = ReadTelemetry

### Save Telemetry Log to Excel
print(TelemetryLog)
TelemetryLog.to_excel(TelemetryLogName, index=False)
        
#'''