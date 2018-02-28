import random
import time
import string

import serial


port = '/dev/ttyACM0'
port = '/dev/ttyUSB0'


arduino = serial.Serial(port, 9600, timeout=5)


while True:
    msg = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    print("Message to arduino: {} ".format(msg))
    arduino.write(msg)
    time.sleep(0.1)
    msg = arduino.read(arduino.inWaiting())
    print("Message from arduino: {} ".format(msg))

    time.sleep(1)
