import socket

HOST = '192.168.43.66'
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    reply = s.recv(1024).decode('utf-8')
    print (reply)
