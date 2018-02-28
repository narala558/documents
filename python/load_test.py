import datetime as dt

from t import dummy


i = 0
start = dt.datetime.now()

try:
    while 1:
        dummy.delay()
        i += 1
except KeyboardInterrupt:
    stop = dt.datetime.now()
    delta = stop - start
    conn_per_sec = float(i / (delta.days*24*3600 + delta.seconds))
    print('\n', i,
          '\n', "tasks created for", delta, "seconds",
          '\n', "Tasks created per sec:", conn_per_sec)
