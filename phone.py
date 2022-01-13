

import serial
import time
import sys

recipient = "+905xxxxxxxxx"
message = "Hello, World!"

phone = serial.Serial("/dev/ttyUSB3",  115200, timeout=5) 
print phone.read

phone.write(b'ATZ\r')
time.sleep(0.5)
phone.write(b'AT+CMGF=1\r')
time.sleep(0.5)
phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
time.sleep(0.5)
phone.write(message.encode() + b"\r")
time.sleep(0.5)
phone.write(bytes([26]))
time.sleep(0.5)

phone.close() 
