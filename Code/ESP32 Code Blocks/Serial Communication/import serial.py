import serial

# Open serial port
ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)

# Write data to the serial port
ser.write(b'Hello, device!\n')

# Read response from the serial port
response = ser.readline().decode('utf-8').strip()
print(f"Response: {response}")

# Close the serial port
ser.close()
