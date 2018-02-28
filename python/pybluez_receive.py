import bluetooth


hostMACAddress = '00:1f:e1:dd:08:3d'
hostMACAddress = '24:0A:64:D7:99:AC'
hostMACAddress = '24:0a:64:d7:99:ac'
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    print('Waiting')
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:
    print("Closing socket")
    client.close()
    s.close()
