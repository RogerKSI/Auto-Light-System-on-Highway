import socket
from gpiozero import LED
from time import sleep
from threading import Thread

#############################################################			
# define variables
#############################################################			
global HOST
global PORT
cycleNumber = 2
cycleTime   = 1
pinLight    = [0,21,20,16,12,7,8,25,24,23,18]
machineNo   = 2
HOST        = '192.168.1.1'
PORT        = 12345
LEDNumber   = 10
light       = [0] * (LEDNumber + 1)
led         = [None] * (LEDNumber + 1)
for i in range(LEDNumber,0,-1):
	led[i] = LED(pinLight[i])
#############################################################			


class ControlSocket:  
	def __init__(self):
		self._running = True

	def terminate(self):  
		self._running = False  

	def run(self):
		global HOST
		global PORT
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST,PORT))
		while self._running:
			reply = s.recv(1024).decode('utf-8')
			if(int(reply) + 1 == machineNo):
				light[1] = light[1] + 1
		
    
#############################################################			
# initial and start ControlSocket thread
#############################################################			
controlSocket = ControlSocket()
controlSocketThread = Thread(target=controlSocket.run) 
controlSocketThread.start()
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
		else:
			led[i].off()

		if(i != 1 and light[i-1] > 0):
			light[i] = light[i] + 1
	
	sleep(cycleTime)
#############################################################
	
