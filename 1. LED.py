'''import RPi.GPIO as GPIO
import time

x = 1
numTimes = int(input("Enter total number of times to blink:"))
speed = float(input("Enter length of each blink(seconds):"))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)

def Blink(numTimes,speed):
    for i in range(0,numTimes):
        GPIO.output(5,True)        #For blinking
        print("Iteration(Blink)",(i+1))
        
        GPIO.output(5,False)      #To stop blinking
        print("Iteration(Off)",(i+1))
        time.sleep(speed)
        
Blink(numTimes,speed)
print("Done")
'''
'''
After saving shutdown the pc, off the buttons.
make connection as below:
Anode(Big Wire) --> Connect to Pin 5
Cathode(Small Wire) ---> Connect to Pin 6
After connection start the computer run the program.

'''

import RPi.GPIO as GPIO
import time

x = 1
numTimes = int(input("Enter total number of times to blink:"))
speed = float(input("Enter length of each blink(seconds):"))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
#GPIO.setup(29,GPIO.OUT)

def Blink(numTimes,speed):
    for i in range(0,numTimes):
        GPIO.output(5,True)        #For blinking
        print("Iteration(Blink)",(i+1))
        GPIO.output(10,True)        #For blinking
        print("Iteration(Blink)",(i+1))
        GPIO.output(19,True)        #For blinking
        print("Iteration(Blink)",(i+1))
        GPIO.output(26,True)        #For blinking
        print("Iteration(Blink)",(i+1))
        #GPIO.output(29,True)        #For blinking
        #print("Iteration(Blink)",(i+1))
        
        GPIO.output(5,False)      #To stop blinking
        print("Iteration(Off)",(i+1))
        time.sleep(speed)
        GPIO.output(10,False)      #To stop blinking
        print("Iteration(Off)",(i+1))
        time.sleep(speed)
        GPIO.output(19,False)      #To stop blinking
        print("Iteration(Off)",(i+1))
        time.sleep(speed)
        GPIO.output(26,False)      #To stop blinking
        print("Iteration(Off)",(i+1))
        time.sleep(speed)
        #GPIO.output(29,False)      #To stop blinking
        #print("Iteration(Off)",(i+1))
        #time.sleep(speed)
        
Blink(numTimes,speed)
print("Done")
