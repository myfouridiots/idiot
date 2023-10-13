'''
Go to terminal and type:
sudo nano /boot/config.txt

then [all] is appear below it type the code in terminal: 
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1

Then press CTRL+O then press enter
press ctrl+x

Now type:
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl enable serial-getty@ttyAMA0.service
sudo apt-get install minicom (NOTE: do you want to continue? Type Y)
sudo pip install pynmea2
sudo cat /dev/ttyAMA0

Type the below code
'''

import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
port = "/dev/ttyAMA0"

ser = serial.Serial(port,baudrate=9600,timeout=0.5)
while 1:
    try:
        data = ser.readline()
        print(data)
    except:
        print("loading")
        
    if data[0:6]=='$GPGGA':
        msg=pynmea2.parse(data)
        print(msg)
        time.sleep(2)
        
'''
Run in Terminal: go to directory where code is saved and type
sudo python GPS.py

Connections with GPS Module:
Pin 2 = VCC
Pin 6 = GND
Pin 10 = TX
'''
