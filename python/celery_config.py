import sys

from celery import Celery


sys.path.append('/etc/celery/')


app = Celery()
app.config_from_object('config')
