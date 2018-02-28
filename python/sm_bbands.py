import numpy as np
import pandas as pd

from nsepy import get_history

import matplotlib

matplotlib.pyplot.show()


def stock_price_df(symbol):
    file = 'data/{}'.format(symbol.upper())
    if not os.path.exists(file):
        time.sleep(5)
        df = get_history(symbol, end=now, start=start)
        df.to_csv(file)
    return pd.read_csv(file)


def bbands(price, length=30, numsd=2):
    """ returns average, upper band, and lower band"""
    ave = pd.stats.moments.rolling_mean(price,length)
    sd = pd.stats.moments.rolling_std(price,length)
    upband = ave + (sd*numsd)
    dnband = ave - (sd*numsd)
    return np.round(ave,3), np.round(upband,3), np.round(dnband,3)


df2 = pd.DataFrame()

df = stock_price_df('acc')
_, df2['upper'], df2['lower'] = bbands(df.Close, length=30, numsd=1)
df2['close'] = df['Close']
df2.plot()

print('done')
# print(df.head(100))
