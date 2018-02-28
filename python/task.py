import os

from celery import Celery


broker = 'amqp://guest@localhost//'

app = Celery(broker=broker)


@app.task
def add(x, y):
    return x + y
