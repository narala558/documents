from celery import Celery
from celery.signals import task_success


app = Celery(broker='amqp://guest@localhost//', backend='rpc')


app.conf.update({
    'CELERYD_LOG_COLOR': False,
})


@app.task
def add(x, y):
    return x + y


@app.task
def wait(seconds):
    print('started')
    print(seconds)
    print('done')


# @task_success.connect(sender='celery_signals.add')
@task_success.connect()
def task_success_handler(sender=None, headers=None, body=None, **kwargs):
    print((sender.request.id))
    print((sender.request.task_id))
    result = kwargs['result']
    print(result)
    print(kwargs)
    print('aaaaaaaaa')
