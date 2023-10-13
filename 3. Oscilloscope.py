'''

https://circuitdigest.com/microcontroller-projects/raspberry-pi-based-oscilloscope

Preferences ---> Raspberry Pi Configuration --> Intefaces --> I2C ---> Enable
Or go to terminal --> sudo raspi-config
When configuration panel opens, select interface option, select I2C and click enable

Update Raspberry Pi type command in terminal:
sudo apt-get update
sudo apt-get upgrade

In upgrade it will ask: Do you want to continue [Y,n]? type Y

Then in terminal type
cd~  (or cd ..)

sudo apt-get install build-essential python-dev python3-smbus git
(mcc@raspberrypi:/home $ sudo apt-get install build-essential python-dev python3-smbus git)

Type in terminal :
cd ~
git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git

(mcc@raspberrypi:/home $ cd ~
mcc@raspberrypi:~ $ git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git)

cd Adafruit_Python_ADS1x15
sudo python3 setup.py install

Connections:
VDD -- Pin 1
GND -- Pin 6
SCl -- Pin 3
SDA -- Pin 5
cd examples
python3 simpletest.py

GO to base directory:
sudo apt-get install python3-matplotlib
mcc@raspberrypi:~ $ sudo apt-get install python3-matplotlib

In terminal type : sudo nano scope.py
If code not found , then type:

import time
import matplotlib.pyplot as plt
from drawnow import *
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = [ ]
cnt = 0
plt.ion()
adc.start_adc(0,gain=GAIN)
print('Reading ADS1x15 channel 0')
def makeFig():
    plt.ylim(-5000,5000)
    plt.title('Oscilloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val,'ro-',label='lux')
    plt.legend(loc = 'lower right')
while (True):
    value=adc.get_last_result()
    print('channel 0:{0}',format(value))
    time.sleep(0.5)
    val.append(int(value))
    drawnow(makeFig)
    plt.pause(.000001)
    cnt = cnt+1
    if(cnt>50):
        val.pop(0)

'''