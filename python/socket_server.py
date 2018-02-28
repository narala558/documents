import socket
import time


s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("Socket binded to {}".format(port))

s.listen(5)
print("Listening...")


while True:
    try:
        c, addr = s.accept()
        print('Got connection from {}'.format(addr))
        c.send(b'Thank you for connecting')
        print(c.recv(10))
        time.sleep(2)
        c.close()
    except KeyboardInterrupt:
        print('key board interrupt \n\n\n\n')
        s.close()
