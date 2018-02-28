import os
import sys
import time
import datetime as dt

import numpy as np
import pandas as pd
import nsepy
from stocktrends import Renko


if len(sys.argv) > 1:
    fname = sys.argv[1]
    print('Reading local file {}'.format(fname))
    df = pd.read_csv(sys.argv[1])
else:
    symbol='SBIN'
    print('Downloading {} data from nsepy'.format(symbol))
    df = nsepy.get_history(
        symbol=symbol,
        start=dt.date(2017,1,1),
        end=dt.date(2018,1,19)
    )
    if df.empty:
        print('No data is received from nsepy.')
        sys.exit()

debug = True
# print(df.tail(20))

renko = Renko(df)
renko.brick_size = 4
r = renko.get_bricks()
print(r.tail(33))
