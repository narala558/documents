import time

from pwm import *
from gpio import *


MOTOR = 1

pwm_export_channel(MOTOR)

period = 10 * 1000 * 1000
duty = 7 * 1000 * 1000
duty = 2 * 1000 * 1000

pwm_set_period(MOTOR, period)
pwm_set_dutycycle(MOTOR, duty)

pwm_enable(MOTOR)

time.sleep(5)
pwm_disable(MOTOR)

pwm_unexport_channel(MOTOR)
