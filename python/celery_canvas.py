from celery import Celery, chain, group, chord
from celery.signals import task_success


app = Celery(broker='amqp://guest@localhost//', backend='amqp://')

app.conf.update({
    'CELERYD_LOG_COLOR': False,
})


@app.task
def add(x, y):
    return x + y


@app.task
def sub(x, y):
    return x - y


@app.task
def get_links_from_website():
    return list(range(10))


@app.task
def download_sub_page(*args):
    return args


@app.task
def process_sub_page(*args):
    return args


@app.task
def upload_sub_page(*args):
    return args


@app.task
def mark_website_done(*args):
    return args


ch = chain(
    download_sub_page.s(),
    process_sub_page.s(),
    upload_sub_page.s(),
)


@task_success.connect(sender='celery_canvas.get_links_from_website')
def task_success_handler(sender=None, headers=None, body=None, **kwargs):
    result = kwargs['result']
    print(result)
    header = [ch(i) for i in result]
    callback = mark_website_done.si()
    chord(header)(callback)
