import socket
from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep
from threading import Thread

#############################################################			
# define variables
#############################################################			
global light
global cycleNumber
global pinPIR
cycleNumber = 2
cycleTime   = 1
pinLight    = [0,21,20,16,12,7,8,25,24,23,18]
machineNo   = 1
HOST        = '192.168.1.1'
PORT        = 12345
pinPIR      = 10
LEDNumber   = 10
light       = [0] * (LEDNumber + 1)
led         = [None] * (LEDNumber + 1)
for i in range(LEDNumber,0,-1):
	led[i] = LED(pinLight[i])
#############################################################			

class ControlPIR:  
	def __init__(self):
		self._running = True

	def terminate(self):  
		self._running = False  

	def run(self):
		global light
		global cycleTime
		global cycleNumber
		pir = MotionSensor(pinPIR)
		while self._running:
			pir.wait_for_motion()
			light[1] = cycleNumber
			#sleep(cycleTime)

			
#############################################################			
# initial and start ControlLED thread
#############################################################			
controlPIR = ControlPIR()
controlPIRThread = Thread(target=controlPIR.run) 
controlPIRThread.start()
#############################################################			
			
			
#############################################################			
# initial socket
#############################################################			
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
try:
	s.bind((HOST, PORT))
except socket.error:
	print ('Bind failed')   

s.listen(1)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print ('Connected')
#############################################################			


#############################################################			
# process LED
#############################################################			
while True:
	print(light)

	for i in range(LEDNumber,0,-1):
		if(light[i] > 0):
			led[i].on()
			light[i] = light[i] - 1
			
			if(i==LEDNumber):
				word = '1'
				conn.sendall(word.encode('utf-8'))
		else:
			led[i].off()

		if(i != 1 and light[i-1] > 0):
			light[i] = light[i] + 1
	
	sleep(cycleTime)
#############################################################

			
#############################################################			
# initial down 
#############################################################			
conn.close()
#############################################################			
