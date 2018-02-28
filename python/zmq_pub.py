import random
import time

import zmq


port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:{}".format(port))


while True:
    topic = random.randrange(100, 105)
    messagedata = random.randrange(1, 99)
    print("{} {}".format(topic, messagedata))
    socket.send_string("{} {}".format(topic, messagedata))
    time.sleep(1)
