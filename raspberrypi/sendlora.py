# run script as super user (e.g. $ sudo python3 sendlora.py)
import serial

data = b"test data"

with serial.Serial('/dev/serial0', 115200, timeout=10) as ser:
    ser.write(data)

print("Data Sent")
