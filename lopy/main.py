from machine import UART
import pycom
import time
from network import LoRa # because obviously we need that
import socket # and that too
import binascii # ... well ... usefull for the hex keys
import struct # ... I don't even remember why I've imported that ...

pycom.heartbeat(False) # turn off heartbeat (can be scary as you don't if it's alive or not until you send something)

uart = UART(1, 115200, bits=8, parity=None, stop=1) # setting up the uart port (do NOT use USB cable. use ONLY for monitoring)
uart.write("Connected...") # tell to any one who's watching that we acctually have something working

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)
app_eui = binascii.unhexlify('7079636f6d303031') # your gateway EUI KEY (in hex)
app_key = binascii.unhexlify('6c6f7079636f6d72756c657332303137') # your gateway MAIN KEY (in hex)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0) # lora auth packet crafting recipe


# connecting to the lora gateway
while not lora.has_joined():
    time.sleep(2.5)
    print('Searching for network...')

print("Connected to the network.")
# connection OK
# let's move 


def send_lora(data): # function to send the data out using the lora antenna
    print("Sending " + data)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    s.send(data) # sending data out in the air ( Weeeeeeeeeee XD )
    s.setblocking(False)
    uart.write(b'Success') # send success feed back to the RPI

while True: # do it until THE END OF THE WORLD !
    if uart.any(): # waiting for data from the RPI3
        data = uart.readall() # the data from the uart
        pycom.rgbled(0xFF0000) # set LED to RED on if data received
        send_lora(str(data)) ############# I acctually don't know why the packet in string looks like " b'something' " but it's working
        pycom.rgbled(0x00FF00) # set LED to GREEN if data is b'send'
        time.sleep(1) # cool down timer (need a drink ?)
        pycom.rgbled(0x000000) # RGBled off
