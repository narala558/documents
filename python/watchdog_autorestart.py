import os
import shlex
import subprocess
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

directory = os.getcwd()
command = 'celery worker -A t -l INFO'


class PyHandler(PatternMatchingEventHandler):

    def process(self, event):
        cmd = 'pkill celery'
        subprocess.call(shlex.split(cmd))
        print('Killed old worker')
        run_worker()

    def on_modified(self, event):
        self.process(event)

def run_worker():
    print("Starting worker: {} ".format(command))
    subprocess.Popen(shlex.split(command))


if __name__ == "__main__":

    run_worker()

    event_handler = PyHandler(patterns=["*.py"])
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
