import threading
from time import sleep

import requests


def foo():
    print('start')
    sleep(10)
    requests.get('http://avilpage.com')
    print('done')


def bar():
    t = threading.Thread(target=foo)
    t.start()
    print('main')

bar()
