import serial
import time
import pandas as pd

"""
read instructions
"""
a=pd.read_excel('instructions.xlsx')
print(a)
for index, row in a.iterrows():
      '''
      for i in ["gLED1","gLED2","yLED","rLED"]:
        if i == "gLED1":
            print(row["gLED1"])
            '''
      


"""
Serial Port Communication with Arduino
"""
# Set up the serial connection (adjust COM port and baud rate as necessary)
ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with your Arduino's port
time.sleep(2)  # Wait for the connection to initialize

# Clear the serial buffers to avoid residual data
ser.reset_input_buffer()
ser.reset_output_buffer()
ser.read_all()

# String to send
data_to_send = "[1, 2, 3, 4, 5]"

# Send the string

ser.write(data_to_send.encode() + b'\n')

# Wait for the response

response = ser.readline().decode("utf-8", errors="ignore").strip()

# Print the received data
print("Received from Arduino:", response)

# Close the serial connection
#ser.close()
