# Importing Libraries 
import serial 
import time 
esp = serial.Serial(port='COM4', baudrate=115200, timeout=.1) 
def write_serial(x): 
                esp.write(bytes(x, 'utf-8'))

def read_serial(): 
        while esp.in_waiting == 0:
               pass
        if esp.in_waiting > 0:  # Check if there's data available
            data = esp.read(esp.in_waiting).decode('utf-8')  # Read and decode the data
            print(data)

while True: 
        num = input("Enter a number: ") # Taking input from user 
        value = write_serial(num)
        time.sleep(.05)
        read_serial()
