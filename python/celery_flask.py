from flask import Flask
from celery import Celery


def make_celery(app):
    celery = Celery(broker='amqp://guest@localhost//', backend='rpc')
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


app = Flask(__name__)

celery = make_celery(app)


class Stuff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    processed = db.Column(db.Boolean)


@celery.task()
def process_stuff(stuff_id):
    stuff = Stuff.query.get(stuff_id)
    print("stuff.processed: {}".format(stuff.processed))
    stuff.processed = True
    print("stuff.processed: {}".format(stuff.processed))
    db.session.add(stuff)
    db.session.commit()
    print("stuff.processed: {}".format(stuff.processed))

@app.route("/process_stuff/<id>")
def do_process_stuff(id):
    stuff = Stuff.query.get_or_404(id)
    process_stuff.delay(stuff.id)
    return redirect(url_for("now_wait"))
