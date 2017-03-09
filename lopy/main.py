from machine import UART
import pycom
import time
from network import LoRa
import socket
import binascii
import struct

pycom.heartbeat(False) # turn off heartbeat

uart = UART(1, 115200, bits=8, parity=None, stop=1)
uart.write("Connected...")

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)
app_eui = binascii.unhexlify('7079636f6d303031')
app_key = binascii.unhexlify('6c6f7079636f6d72756c657332303137')
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    time.sleep(2.5)
    print('Searching for network...')

print("Connected to the network.")

def send_lora(data):
    print("Sending " + data)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    s.send(data)
    s.setblocking(False)
    uart.write(b'Success')

while True:
    if uart.any():
        data = uart.readall()
        pycom.rgbled(0xFF0000) # set LED to RED on if data received
        send_lora(str(data)) ############# not sure it's the we need it to work ...
        pycom.rgbled(0x00FF00) # set LED to GREEN if data is b'send'
        time.sleep(1)
        pycom.rgbled(0x000000)
