from celery import Celery


app = Celery('test')

print(app.platforms)

app.start(
    argv=['celery', 'worker', '-l', 'info', '-n', 'foo_worker']
)
