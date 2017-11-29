# It will work when monitor is connected to the Pi

# How to enable camera
#   - sudo raspi-config
#   - choose 'interfacing options'
#   - choose 'P1 Camera'
#   - select 'yes'

from picamera import PiCamera
from time import sleep

camera = PiCamera() # initial

# config parameter
camera.rotation = 180 # rotate video
camera.framerate = 15
camera.resolution = (640,480)

camera.start_preview() # show video

# capture image and save
for i in range(5):
    sleep(5)
    camera.capture('/home/pi1/Desktop/image%s.jpg' %i)

# save video
# You can play video by using 'oxmplayer video.h264' command
camera.start_recording('home/pi1/video.h264')
sleep(10)
camera.stop_recording()


camera.stop_preview()
