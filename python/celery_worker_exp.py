from celery import Celery
from celery.signals import worker_process_init


app = Celery(
    'tasks',
    broker='amqp://guest@localhost//',
    backend='rpc://',
)


@worker_process_init.connect()
def setup(**kwargs):
    print('initializing NLP parser')
    # setup
    print('done initializing NLP parser')


@app.task
def add(x, y):
    print(x, y)
    return x + y
