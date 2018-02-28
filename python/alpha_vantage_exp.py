import os

import stocktrends
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

key = os.environ.get('ALPHAVANTAGE_KEY')
print(key)

ts = TimeSeries(key=key, output_format='pandas')

symbol = 'NSE:RELIANCE'

df, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='compact')
renames = {
    '1. open': 'open',
    '2. high': 'high',
    '3. low': 'low',
    '4. close': 'close',
    '5. adjusted close': 'adjusted close',
    '6. volume': 'volume',
    '7. dividend amount': 'dividend amount',
    '8. split coefficient': 'split coefficient'
}
df.rename(columns=renames, inplace=True)

df.to_csv('tmp.csv')
df = pd.read_csv('tmp.csv')
renko = stocktrends.Renko(df)
renko.brick_size = 9.5
r = renko.get_bricks()
print(r.head())
