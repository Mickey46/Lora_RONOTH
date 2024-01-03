import serial
import time

# Configure the serial connection
ser = serial.Serial('/dev/ttyUSB2', baudrate=57600, timeout=1)

# Function to send a command to the LoRa stick
def send_command(command):
    ser.write((command + '\r\n').encode())
    time.sleep(1)
    return ser.read_all().decode()

# Initialize LoRa stick
send_command('sys reset')
send_command('mac pause')
send_command('radio set mod lora')
send_command('radio set freq 915000000')  # Set to your region's frequency
send_command('radio set pwr 14')

# Receive a message
send_command('radio rx 0')

while True:
    response = ser.readline()
    if response:
        print("Received: " + response.strip().decode())
        break
