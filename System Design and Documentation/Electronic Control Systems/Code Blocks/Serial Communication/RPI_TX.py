import serial
import time

# Set up the serial connection (adjust COM port and baud rate as necessary)
ser = serial.Serial('COM8', 115200)  # Replace 'COM3' with your Arduino's port
time.sleep(2)  # Wait for the connection to initialize

# Clear the serial buffers to avoid residual data
ser.reset_input_buffer()
ser.reset_output_buffer()

# String to send
data_to_send = "[1, 2, 3, 4, 5]"

# Send the string
ser.write(data_to_send.encode() + b'\n')

# Wait for the response
response = ser.readline().decode().strip()

# Print the received data
print("Received from Arduino:", response)

# Close the serial connection
#ser.close()
