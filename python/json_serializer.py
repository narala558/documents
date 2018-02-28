import json
import time
from datetime import datetime
from time import mktime

from celery import Celery
from kombu.serialization import register


class Website:
    def __init__(self, url):
        self.url = url


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return {
                '__type__': '__datetime__',
                'epoch': int(mktime(obj.timetuple()))
            }
        else:
            return json.JSONEncoder.default(self, obj)


def my_decoder(obj):
    if '__type__' in obj:
        if obj['__type__'] == '__datetime__':
            return datetime.fromtimestamp(obj['epoch'])
    return obj

# Encoder function
def my_dumps(obj):
    return json.dumps(obj, cls=MyEncoder)

# Decoder function
def my_loads(obj):
    return json.loads(obj, object_hook=my_decoder)


# register('myjson', my_dumps, my_loads,
#     content_type='application/x-myjson',
#     content_encoding='utf-8')

app = Celery(broker='amqp://guest@localhost//', backend='amqp://')

serializer = 'myjson'
serializer = 'myjson'
# serializer = 'json'
app.conf.update({
    'CELERY_SEND_EVENTS': False,
    'CELERYD_LOG_COLOR': False,
    'CELERY_ACCEPT_CONTENT': [serializer],
    'CELERY_TASK_SERIALIZER': serializer,
    'CELERY_RESULT_SERIALIZER': serializer,
})


@app.task
def add(x, y):
    return x + y


@app.task
def wait(seconds):
    print('started')
    time.sleep(seconds)
    print('done')
