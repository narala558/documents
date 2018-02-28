import json
import time
from json import JSONEncoder

from celery import Celery
from kombu.serialization import register


class Website:
    def __init__(self, url):
        self.url = url


class WEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Website):
            d = {
                '__type__': '__website__',
                'url': Website.url,
            }
            return d
        else:
            return JSONEncoder.default(self, obj)


def w_decoder(obj):
    if '__type__' in obj:
        if obj['__type__'] == '__website__':
            return Website(obj['url'])
    return obj


def w_dumps(obj):
    return json.dumps(obj, cls=WEncoder)


def w_loads(obj):
    return json.loads(obj, object_hook=w_decoder)


register(
    name='myjson',
    encoder=w_dumps,
    decoder=w_loads,
    content_type='application/x-myjson',
    content_encoding='utf-8'
)


def loads(s):
    return s


def dumps(s):
    return s


register(
    'mem_serializer', dumps, loads,
    content_type='application/x-memory',
    # content_encoding='utf-8',
    content_encoding='binary',
)


app = Celery(broker='redis://localhost:6379/0')

serializer = 'myjson'
serializer = 'mem_serializer'
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
