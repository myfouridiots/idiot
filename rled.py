import RPi.GPIO as GPIO
import time

x=1
numTimes=int(input("Enter total number of times to blink"))
speed=float(input("Enter length of each blink(seconds):"))
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
            
def Blink(numTimes,speed):
    for i in range(0,numTimes):
            GPIO.output(5,True)
            print("Iteration", i+1)
            time.sleep(speed)
            GPIO.output(5,False)
            print("Iteration", i+1)
            time.sleep(speed)
Blink(numTimes, speed)
print("Done")
