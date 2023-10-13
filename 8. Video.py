import picamera
from time import sleep
camera=picamera.PiCamera()
camera.resolution=(640,480)
print()
camera.start_recording("/home/pi/demo.h264")
camera.wait_recording(20)
camera.stop_recording()
camera.close()
print("Video recording stopped")

'''
To play the video command:
Omxplayer demo.h264
'''