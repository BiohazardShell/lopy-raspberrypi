# run script as super user (e.g. $ sudo python3 sendlora.py)
import serial

data = "new entery 01".encode()

with serial.Serial('/dev/serial1', 115200, timeout=10) as ser:
    ser.write(data)

print("Data Sent")
