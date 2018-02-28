import os

from celery import Celery

remote_broker = os.environ.get('BROKER_URL')
remote_broker = 'amqp://staging:staging@130.211.198.20/'
# remote_broker = 'amqp://guest:guest@130.211.198.20/'

app = Celery('avilpage', broker=remote_broker)

print(app.broker_connection())


@app.task
def add(x, y):
    return x + y
