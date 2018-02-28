from datetime import date, datetime, timedelta

from nsepy import get_history
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

close = 'Close'
change = 'change'


def plot_column(df, col):
    fig, ax = plt.subplots()
    ax.plot(df.index, df[col])
    # df.plot(y='gizmos', ax=ax)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    fig.set_size_inches(16, 8)
    plt.show()


def show_stats(df):
    df[change] = round((1 - df[close] / df[close].shift(1)) * 100, 2)
    df[change] = df[change].shift(-1)

    print("daily")
    print("abs mean", np.mean(df[change].abs()))
    print("mean", np.mean(df[change]))
    print("std ", np.std(df[change]))

    duration = 5
    print(duration)
    davg = np.mean(df[change]) * duration
    dstd = np.std(df[change]) * (duration ** 0.5)
    rmin = davg - dstd
    rmax = davg + dstd
    print(rmin, rmax)

    return df


now = datetime.now()
today = now.date()


# start_date = date(2016, 1, 1)
start_date = today - timedelta(365)

# end_date = date(2015,7,1)
end_date = today

print(start_date, end_date)


symbol = "NIFTY"
symbol = 'acc'
# symbol = "BANKNIFTY"
print(symbol)

# df = get_history(
#     symbol=symbol, index=True,
#     start=start_date, end=end_date,
# )


import time

def get_stock_df(symbol):
    file = 'data/{}'.format(symbol.upper())
    if not os.path.exists(file):
        time.sleep(5)
        df = get_history(symbol, end=now, start=start_date)
        df.to_csv(file)
    return pd.read_csv(file)

df = get_stock_df(symbol)
df = df.sort_index(ascending=False)

# print(df.head())
#df.drop(['High'], inplace=True)
#df.drop('High', 1, inplace=True)
#df = df.drop('Low', axis=1)

dr = 'daily_returns'
df[dr] = df['Close'] / df['Open'] - 1
# plot_column(df, dr)

# ldr = 'log_daily_returns'
# df[ldr] = np.log(df['Close'] / df['Open'])
# plot_column(df, ldr)


dv = np.std(df[dr]) * 100
av = dv * (365**(1 / 2))
print("daily vol, annual vol", dv, av)


df = show_stats(df)
# print(df.head(10))

# df.hist(column=change, bins=100)


def add_chgp(df, col, col_diff):
    print('a')
    df[col_diff] = round((1 - df[col] / df[col].shift(-1)) * 100, 2)
    df[col_diff] = df[col_diff].shift(1)
    return df


close = 'Close'
close_diff = 'close_diff'
close_chgp = 'close_chgp'

df = add_chgp(df, close, close_chgp)
print(df.columns)

print(df[[close, close_chgp]])

df['date'] = df.index

# df.set_index(list(range(len(df))))


print(df[close_chgp].groupby(df.index / 5).mean())

print(df[close_chgp].sum())
