import time

from celery import Celery


app = Celery(
    'tasks',
    broker='pyamqp://guest@localhost//',
)

app.conf.result_backend = 'redis://localhost:6379/0'



@app.task
def add(x, y):
    return x + y


@app.task
def wait(seconds):
    print('started')
    time.sleep(seconds)
    print('done')


@app.task
def foo(*args, **kwargs):
    print(args, kwargs)
