import serial
import time
import pandas as pd


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

#String to send

b=""

#Build Readout String
for i, row in Instructions.iterrows():
    package = "WI;"

    for item in Instructions.columns:
        pass
        #print(item)
        #print(row[item])
        #print(PackageLabelKey[str(item)])
        package += PackageLabelKey[item] + ":" + str(row[item]).strip() + ";"

    print("sent: " + package)
    ser.write(package.encode() + b'\n')
    response = ser.readline().decode("utf-8", errors="ignore").strip()
    print("Received from Arduino:", response)
#'''