# run script as super user (e.g. $ sudo python3 sendlora.py)
import serial # because you know ... you need to talk

data = "data to send trought the lora".encode() # ... well ... it's obvious ... I think ...

with serial.Serial('/dev/ttyAMA0', 115200, timeout=10) as ser: # remember to change the timeout from 10 sec to lower if you want it to speed up
    ser.write(data) # data out trought the Tx . good job !

print("Data Sent") # In case you want to know ...
