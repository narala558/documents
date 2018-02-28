import random
import time

import redis


r = redis.client.StrictRedis()

channels = ['c1', 'c2', 'c3']
messages = ['m1', 'm2', 'm3']

while True:
    channel = random.choice(channels)
    message = random.choice(messages)
    print('Publishing {} on {}'.format(message, channel))
    r.publish(channel, message)
    time.sleep(1)
