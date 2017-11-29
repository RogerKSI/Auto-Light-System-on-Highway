import socket

HOST = '192.168.1.1'
PORT = 12345
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

while True:
    word = input('Enter word: ')
    if word == 'quit':
        break

    conn.sendall(word.encode('utf-8'))
    
conn.close()
