from celery import Celery


broker = 'memory://'
broker = 'sqla+postgresql://f:f@localhost/f'
broker = 'amqp://guest:guest@localhost//'
broker = 'redis://localhost:6379/0'

app = Celery(broker=broker)

app.conf.update({
    'CELERYD_LOG_COLOR': False,
})


@app.task
def add(x, y):
    return x + y


@app.task
def dummy():
    pass
