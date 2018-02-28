import time

from celery import Celery, states

app = Celery(broker='amqp://guest@localhost//', backend='rpc')
# app = Celery(broker='redis://localhost:6379/0')

app.conf.update({
    'CELERYD_LOG_COLOR': False,
})


@app.task
def add(x, y):
    return x + y


@app.task(bind=True)
def fail(self):
    self.update_state(
        task_id=self.request.id,
        state=states.FAILURE,
        meta="result is None"
    )
    raise Ignore()


@app.task
def wait(seconds):
    print('started')
    time.sleep(seconds)
    print('done')


@app.task
def foo(*args, **kwargs):
    print(args, kwargs)
