import time


from celery import Celery
from celery.signals import task_retry


app = Celery(broker='amqp://guest@localhost//', backend='amqp://')


@app.task
def sub(x, y):
    time.sleep(60)
    return x - y


@app.task(bind=True)
def add(self, x, y):
    try:
        print(e)
    except Exception as e:
        self.retrying = True
        self.retry(countdown=20, exc=e)
    return x + y


retries = []


@task_retry.connect()
def track_retries(*args, **kwargs):
    import ipdb; ipdb.set_trace()

    print(kwargs['request']['id'])
