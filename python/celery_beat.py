from datetime import timedelta

from celery import Celery


app = Celery(broker='amqp://guest@localhost//', backend='amqp://')

app.conf.update({
    'worker_log_color': False,
})


@app.task
def add(x, y):
    return x + y


app.conf.beat_schedule = {
    'cntv-test': {
        'task': 'beat.add',
        'schedule': timedelta(seconds=10),
        'args': (1, 2),
    },
}
