from celery import Celery


from kombu import Exchange, Queue
from kombu.common import Broadcast


app = Celery(broker='amqp://guest@localhost//', backend='rpc://')

bc_exchange = Exchange('bq', type='fanout')
bc_queue = 'bq'

app.conf.task_queues = (
    # Broadcast(name=bc_queue, exchange=bc_exchange, routing_key='bq'),
    Broadcast(name=bc_queue),
)


@app.task
def factor(number):
    print(number)
    return [i for i in range(1, number + 1) if number % i == 0]
