# run script as super user (e.g. $ sudo python3 sendlora.py)
import serial

data = "new entery 01".encode()

with serial.Serial('/dev/serial1', 115200, timeout=10) as ser:
    ser.write(bytes_data) # need to find a way to send variables like the data ubove

print("Data Sent")
