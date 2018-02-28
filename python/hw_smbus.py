import smbus
from time import sleep


BUSNO = 0
SLAVE = 0x1c
REG = 1

i2c = smbus.SMBus(BUSNO)
i2c.open(BUSNO)

data = i2c.read_byte_data(SLAVE, REG)
print(data)


CTRL_REG1 = 0x2A    # Accelerometer control reg to set enable mode.
ENABLE = 0x01       # Enable bit.
SCALE = 2 / 128     # Acceleration is from +128 to -128


def twos_complement(data):
    if data & 0x80:
        return -((~data & 0xFF) + 1)
    else:
        return data


acc = smbus.SMBus(BUSNO)
acc.open(BUSNO)

acc.write_byte_data(ACC_ADDR, CTRL_REG1, ENABLE)
acc.write_byte(ACC_ADDR, 0x00)

while True:
    data = acc.read_i2c_block_data(ACC_ADDR, 0x00)
    x = twos_complement(data[1]) * SCALE
    y = twos_complement(data[3]) * SCALE
    z = twos_complement(data[5]) * SCALE

    print("x={0:.2}g y={1:.2}g z={2:.2}g".format(x, y, z))

    sleep(1)
