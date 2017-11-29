from gpiozero import LED
from time import sleep

led = LED(17) # 17 is GP17 port

while True:
    led.on()    # open LED
    sleep(1)   # wait 1 sec
    led.off()   # close LED
    sleep(1)
