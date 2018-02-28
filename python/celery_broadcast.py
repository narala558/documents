import random

from celery import Celery
from kombu import Exchange
from kombu.common import Broadcast


app = Celery(broker='amqp://guest@localhost//', backend='rpc://')

bc_exchange = Exchange('bq', type='fanout')
bc_queue = 'bq'

app.conf.task_queues = (
    Broadcast(name=bc_queue, exchange=bc_exchange),
)


@app.task
def add(x, y):
    print(x, y)
    print(random.random())
    return x + y
