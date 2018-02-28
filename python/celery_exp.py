from celery import Celery

# cli
# celery status
# celery purge
# celery purge -f


app = Celery(broker='amqp://guest@localhost//')
app = Celery(broker='redis://localhost:6379/0')


@app.task()
def add(x, y):
    return x + y


r = add.delay()
r = add.apply_async(args=[1, 2], eta=datetime(2014, 6, 12, 0, 0))
r = add.apply_async(args=[1, 2], countdown=10)
r = add.apply_async(args=[2, 3], queues='email')



# inspect

from celery.task.control import revoke, inspect, discard_all

i = inspect()
i.scheduled()
i.active()
i.registered()

# revoke task by id
task_id = 'foo'
revoke(task_id, terminate=True)
r = add.apply_async(args=[1, 2])
r.revoke()


# run worker from script
argv = ['worker', '--loglevel=DEBUG']
app.worker_main(argv)


# canvas
# chain, group, chord


# config
CELERYD_LOG_COLOR = False

# disable prefecthing
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_CONCURRENCY = 1
CELERY_ACKS_LATE = True

CELERY_RDB_PORT = 6899


# debugging
rdb.set_trace()
