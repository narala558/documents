import collections
import os
import time
import datetime as dt
from os.path import join
import warnings
import sys

import pandas as pd
from nsepy import get_history
import techind
import sm_kite
import stockstats
from stockstats import StockDataFrame
import prettytable
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

sys.path.append(os.path.expanduser('~/Dropbox/tech/'))
import sm_data

warnings.simplefilter(action='ignore', category=FutureWarning)

close = 'close'
avg = 'average'
ma = 'moving_average'

now = dt.datetime.now()
today = now.date()
# start_date = date(2016, 1, 1)
start_date = today - dt.timedelta(3650)

print()

renko = 'RENKO'


def atr_status(df):
    # df = techind.ATR(df, 7)
    df = StockDataFrame.retype(df)
    _ = df['close_21_ema']
    _ = df['atr_7']

    df['atr_sl'] = df['close_21_ema'] - df['atr_7'] * 3
    df['atr_sl_status'] = df['close'] > df['atr_sl']
    # df.drop(['open', 'high', 'low', 'close', 'volume'], axis=1, inplace=True)
    # df = df.reset_index()
    # df.drop(['date', 'open', 'high', 'low', 'volume'], axis=1, inplace=True)
    return df
# print(df.tail(1))
# print(df['atr_sl_status'][-1])


def plot_renko(data, brick_size):
    fig = plt.figure(1)
    fig.clf()
    axes = fig.gca()
    y_max = max(data)

    prev_num = 0

    bricks = []

    for delta in data:
        if delta > 0:
            bricks.extend([1]*delta)
        else:
            bricks.extend([-1]*abs(delta))

    for index, number in enumerate(bricks):
        print((index, number), (1, brick_size), number)

        if number == 1:
            facecolor='green'
        else:
            facecolor='red'

        prev_num += number

        renko = Rectangle((index, prev_num * brick_size), 1, brick_size, facecolor=facecolor, alpha=0.5)
        axes.add_patch(renko)


    axis_range = len(bricks)
    major_ticks = np.arange(-axis_range, axis_range, 4)
    minor_ticks = np.arange(-axis_range, axis_range, 1)

    axes.set_xticks(major_ticks)
    axes.set_yticks(major_ticks)
    axes.grid(which='both')

    plt.show()


def renko_status(df):
    df['cdiff'] = df[close] - df[close].shift(1)
    df = df.dropna()
    df['bricks'] = df.loc[:, ('cdiff', )] / brick_size
    df.loc[:, ('bricks', )] = df['bricks'].astype(int)
    df = df[df['bricks'] != 0]

    column = 'bricks'
    bricks = df[column]
    grouper = (bricks != bricks.shift()).cumsum()
    df['rcsum'] = df.groupby(grouper)[column].cumsum()
    df['rdiff'] = df[column].diff()

    return df

symbols = ['acc', 'reliance', 'jvlagro']
symbols = ['reliance', 'icicibank', 'jetairways']
symbols = ['reliance', 'nifty50', 'idea']
symbols = ['reliance']
cache = True
# cache = False

columns = ('symbol', 'close', 'buy_status', 'renko_score', 'brick_size', )
table = prettytable.PrettyTable(columns)

buy_status = 'b'

for symbol in symbols:
    print(symbol)
    print('---------------------')
    df = sm_data.get_stock_df(symbol, cache=cache, provider=1)

    df = atr_status(df)
    print(df.head())
    brick_size = 1.89
    brick_size = df['atr_7'][-1] * 1.2
    df = renko_status(df)
    rscore = df['rcsum'][df['rdiff'].shift(-1) != 0]
    print(df.head())

    bricks = df[df['bricks'] != 0]['bricks'].values
    plot_renko(bricks[-20:], brick_size)
    data = (symbol, df[close][-1], buy_status, rscore[-8:], brick_size)
    table.add_row(data)


print(table)
# print(df['bricks'])
