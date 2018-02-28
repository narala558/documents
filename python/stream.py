import socket

HOST = '0.0.0.0'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
s.close()


with open('f.mp4', 'wb') as fh:
     fh.write(data)
