import zmq


port = "5556"

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from server...")
socket.connect("tcp://localhost:{}".format(port))

# subscribe to all
socket.setsockopt_string(zmq.SUBSCRIBE, '')
# subscribe to anything that starts with 1
socket.setsockopt_string(zmq.SUBSCRIBE, '1')

while True:
    string = socket.recv()
    topic, messagedata = string.split()
    print(topic, messagedata)
