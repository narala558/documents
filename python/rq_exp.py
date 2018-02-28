from redis import Redis
from rq import Queue
from rq.decorators import job


q = Queue(connection=Redis())


def add(x, y):
    return x + y


q.enqueue()
