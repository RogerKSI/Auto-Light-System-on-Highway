from gpiozero import MotionSensor
pir = MotionSensor(4) # 4 mean GP that connect with middle wire


while True:
    print("You moved")
    pir.wait_for_no_motion()
