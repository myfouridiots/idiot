'''
Go to preference -> PI Configuration --> Interface -> Enable I2C
Open Terminal --> type : sudo raspi-config ---> Interface --> Legacy Camera -> Turn On.
'''

import picamera
from time import sleep
camera=picamera.PiCamera()
camera.resolution=(1024,768)
camera.brightness=60
camera.start_preview()
camera.annotate_text = 'Hi Pi User'
sleep(5)
camera.capture('image1.jpeg')
camera.stop_preview()

'''
open new file and type code with name "Video.py"
'''