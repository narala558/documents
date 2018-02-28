import os
import sys
from datetime import date, datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

import pandas as pd
# pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

sys.path.append(os.path.expanduser('~/Dropbox/tech/'))
import sm_data


symbol = "NIFTY"
cache = True
# cache = False


now = datetime.now()
today = now.date()
start = today - timedelta(days=365 * 4)

options = {
    'index': True,
    'start': start,
}

df = sm_data.get_stock_df(symbol, cache=cache, provider=2, options=options)
df.columns = ['open', 'high', 'low', 'close', 'volume', 'turnover']
df.drop(['volume', 'turnover'], axis=1, inplace=True)

df['close_s1'] = df['close'].shift(1)

df['diff_co_pc'] = df['open'] - df['close_s1']
df['diff_co_pc_p'] = round((df['open']/df['close_s1'] - 1)* 100, 2)

df['diff_cl_co'] = df['low'] - df['open']
df['diff_cl_co_p'] = round((df['low']/df['open'] - 1)* 100, 2)

df.dropna(inplace=True)

# df['diff_co_pc_p'] = round(df['diff_co_pc']/df['close'].shift()* 100, 2)
# df['diff_co_pc_p'] = round((1 - df[col] / df[col].shift(-1)) * 100, 2)
# df[col_diff] = df[col_diff].shift(1)

df = df.tail(1000)

print(len(df))
m = df['diff_co_pc_p'].mean()
s = df['diff_co_pc_p'].std()
print(m, s, (m - s, m + s))
print(abs(df['diff_co_pc_p']).mean())



# print(df.head())

# df = df[(df['diff_co_pc_p'] < 1.5) & (df['diff_co_pc_p'] > -1.5)]
# df = df[abs(df['diff_co_pc_p']) < 1]
# df = df[abs(df['diff_co_pc_p']) > 0.3]
print('---')
df = df[df['diff_co_pc_p'] > 0.3]
print(len(df))

print('---')
df = df[df['diff_cl_co_p'] < -0.3]
print(len(df))

# m = df['diff_cl_co_p'].mean()
# print(m)

# df.hist(column='diff_co_pc_p', bins=60)
# plt.show()

# print(df.tail(100))
