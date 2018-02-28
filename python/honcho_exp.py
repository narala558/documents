import sys

from honcho.manager import Manager

m = Manager()
m.add_process('ls', 'python manage.py runserver')
m.loop()

sys.exit(m.returncode)
