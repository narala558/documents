import collections
import os
import time
import datetime as dt
from os.path import join

import pandas as pd

from nsepy import get_history
import techind

close = 'Close'
avg = 'average'
ma = 'moving_average'

now = dt.datetime.now()
today = now.date()
# start_date = date(2016, 1, 1)
start_date = today - dt.timedelta(3650)

print()

stocks_dir = os.path.expanduser('~/.stocks')


def stock_df(symbol):
    file = os.path.join(stocks_dir, symbol.upper())
    if not os.path.exists(file):
        print('Downloading {}'.format(symbol))
        time.sleep(5)
        df = get_history(symbol, end=today, start=start_date)
        df.to_csv(file)
    return pd.read_csv(file)


symbol = 'fconsumer'
symbol = 'jvlagro'
symbol = 'reliance'


def update_stxd(stxd_data, df):
    stxd = 'STXD_7_3'
    if stxd not in df.columns:
        symbol = df.iloc[0]['Symbol']
        print('Calculating stx for {}'.format(symbol))
        df = techind.SuperTrend(df, 7, 3)
        df[stxd] = df['STX_7_3'].diff()

        df.to_csv(os.path.join(stocks_dir, symbol), index=False)

    df = df[df[stxd].isin([2, -2])]

    for row in df.iterrows():
        date = row[1]['Date']
        symbol = row[1]['Symbol']
        lth = 'LOW2HIGH'
        htl = 'HIGH2LOW'

        # print(data[date]['H'], symbol)
        if row[1][stxd] > 0:
            stxd_data[date]['H'].append(symbol)
            stxd_list.append([date, lth, symbol])
        else:
            stxd_data[date]['L'].append(symbol)
            stxd_list.append([date, htl, symbol])


symbols = ['acc', 'reliance', 'jvlagro']

nifty_file = join(stocks_dir, 'NIFTY50.txt')
nifty_symbols = [i.strip() for i in open(nifty_file).readlines()]
nifty_symbols = ['reliance']


stxd_data = collections.defaultdict(lambda: {'L': [], 'H': []})
stxd_list = []

for symbol in nifty_symbols:
    df = stock_df(symbol)
    # print(df.head())
    update_stxd(stxd_data, df)


sdf = pd.DataFrame(stxd_list)
sdf.to_csv('supertrend.csv', index=False)

# for key, value in stxd_data.items():    print(key, value)
# for i in stxd_list:    print(i)
