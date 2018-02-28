import serial


port = '/dev/ttyLP1'

tty = serial.Serial(port, 9600, timeout=5)
msg = b'foo'
tty.write(msg)
