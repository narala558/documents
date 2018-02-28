import os

import redis


r_host = os.environ.get('REDIS_HOST', 'localhost')

r = redis.client.StrictRedis(host=r_host)
s = r.pubsub()

# channels = ['c1', 'c2', 'c3']
# for c in channels:
#     s.subscribe(c)

# s.subscribe(['c1'])

s.psubscribe('*')

while True:
    for m in s.listen():
        print(m)
