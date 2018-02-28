import collections
import os
import time

import pandas as pd

from nsepy import get_history
import matplotlib; matplotlib.pyplot.show()

close = 'Close'
avg = 'average'
ma = 'moving_average'

print()


def stock_df(symbol):
    file = 'data/{}'.format(symbol.upper())
    if not os.path.exists(file):
        time.sleep(5)
        df = get_history(symbol, end=now, start=start)
        df.to_csv(file)
    return pd.read_csv(file)


symbol = 'reliance'
symbol = 'fconsumer'
df2 = stock_df(symbol)

df = pd.DataFrame()
volume = 'Volume'

df[close] = df2[close]
df[volume] = df2[volume]

df['close_diff'] = df[close] - df[close].shift(1)
# df['close_diff_sign'] = df[close_diff] > 0
df['pv'] = df[volume] * df['close_diff'] / 100000
# df['pv_diff'] = df['pv'] - df['pv'].shift(1)
# df['pvd_ewma5'] = pd.ewma(df['pv_diff'], span=5, adjust=adjust)
adjust = True
df['pv_ewma5'] = pd.ewma(df['pv'], span=5, adjust=adjust)

# del df['close_diff']

cls = df[close]


# df['ewma9'] = cls.ewm(span=9)
adjust = False

# df['ewma9'] = pd.ewma(df[close], span=9, adjust=adjust)
# df['ewma12'] = pd.ewma(df[close], span=12, adjust=adjust)
# df['sma20'] = pd.rolling_mean(df[close], window=20)
# df['ewma26'] = pd.ewma(df[close], span=26, adjust=adjust)
# df['MACD'] = df['ewma12'] - df['ewma26']

print(df.tail(15))
print()

df3 = pd.DataFrame()
df3.index = df.index
df3[close] = df[close]
# df3['pv_ewma5'] = df['pv_ewma5']
df3.plot()
