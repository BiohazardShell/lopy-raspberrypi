# run script as super user (e.g. $ sudo python3 sendlora.py)
import serial

data = "new entery 01".encode()

with serial.Serial('/dev/serial1', 115200, timeout=10) as ser: # remember to change the timeout from 10 sec to lower if you wnt it to speed up
    ser.write(data)

print("Data Sent")
