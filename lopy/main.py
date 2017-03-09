from machine import UART
import pycom
import time
from network import LoRa
import socket
import binascii
import struct

pycom.heartbeat(False) # turn off heartbeat

uart1 = UART(1, 115200, bits=8, parity=None, stop=1)
uart1.init(baudrate=115200, bits=8, parity=None, stop=1, timeout_chars=2, pins=("P3", "P4")) # G11(TX) and G24(RX)
uart1.write("Connected...")

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)
app_eui = binascii.unhexlify('7079636f6d303031')
app_key = binascii.unhexlify('6c6f7079636f6d72756c657332303137')
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    time.sleep(2.5)
    print('Searching for network...')

print("Connected to the network.")

# Open LoRaWAN socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(True)

def send_lora(data):
    print("Sending " + data)
    s.send(data)
    uart1.write(b'Success')

while True:
    if uart1.any():
        data = uart1.readall()
        pycom.rgbled(0xFF0000) # set LED to RED on if data received
        send_lora(str(data))
        pycom.rgbled(0x00FF00) # set LED to GREEN if data is b'send'
        time.sleep(1)
        pycom.rgbled(0x000000)
    time.sleep(0.25)
