import time
import sys
import timeit

from celery import Celery


broker = 'memory://'

app = Celery(broker=broker)

app.conf.update({
    'CELERYD_LOG_COLOR': False,
})



@app.task
def add(x, y):
    time.sleep(2)
    return x + y


@app.task
def dummy():
    time.sleep(2)
    pass


tasks = 1000
start_time = timeit.default_timer()
[dummy.delay() for i in range(tasks)]
duration = timeit.default_timer() - start_time
print("Queue rate: " + str(tasks//duration) + " tasks/sec")
