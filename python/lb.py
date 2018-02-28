import sys
import datetime as dt

import numpy as np
import pandas as pd
import nsepy


class LineBreak:

    LINE_NUMBER = 3
    PRICE_MOVEMENT = 2

    TREND_CHANGE_DIFF = 2

    required_columns = {'open', 'high', 'low', 'close'}

    def __init__(self, df):
        self.odf = df
        self.df = df
        self._validate_df()

    def _validate_df(self):
        if not self.required_columns.issubset(self.df.columns):
            raise ValueError('DataFrame should have OHLC {} columns'.format(self.required_columns))

    def uptrend_reversal(self, close):
        lows = [self.cdf.iloc[i]['low'] for i in range(-1, -self.LINE_NUMBER - 1, -1)]
        least = min(lows)
        return close < least

    def downtrend_reversal(self, close):
        highs = [self.cdf.iloc[i]['high'] for i in range(-1, -self.LINE_NUMBER - 1, -1)]
        highest = max(highs)
        return close > highest

    def get_chart_data(self):
        self.df = self.df[['date', 'open', 'high', 'low', 'close']]

        columns = ['date', 'open', 'high', 'low', 'close']

        self.cdf = pd.DataFrame(
            columns=columns,
            data=[],
        )

        for i in range(self.LINE_NUMBER):
            self.cdf.loc[i] = self.df.loc[i]

        self.cdf['uptrend'] = True

        columns = ['date', 'open', 'high', 'low', 'close', 'uptrend']

        for index, row in self.df.iterrows():

            close = row['close']

            row_p1 = self.cdf.iloc[-1]
            row_p2 = self.cdf.iloc[-2]

            uptrend = row_p1['uptrend']

            open_p1 = row_p1['open']
            high_p1 = row_p1['high']

            low_p1 = row_p1['low']
            close_p1 = row_p1['close']

            high_p2 = row_p2['high']
            low_p2 = row_p2['low']

            if uptrend and close > close_p1:
                r = [close_p1, close, close_p1, close]
                t = 'uc'
            elif uptrend and self.uptrend_reversal(close):
                uptrend = not uptrend
                t = 'ur'
                r = [open_p1, open_p1, close, close]
            elif not uptrend and close < close_p1:
                r = [close_p1, close_p1, close, close]
                t = 'dc'
            elif not uptrend and self.downtrend_reversal(close):
                uptrend = not uptrend
                r = [open_p1, close, open_p1, close]
                t = 'dr'
            else:
                continue

            sdf = pd.DataFrame(data=[[row['date']] + r + [uptrend]], columns=columns)
            self.cdf = pd.concat([self.cdf, sdf])

        return self.cdf

    def update_ohlc(self):
        self.df.loc[:, 'close_s1'] = self.df['close'].shift(1)
        self.df.loc[:, 'close_s2'] = self.df['close'].shift(2)

        low = (self.df['close'] < self.df['close_s1']) & (self.df['close'] < self.df['close_s2'])
        # low = self.df['close'] < self.df['close_s2']
        self.df.loc[low, 'close_l'] = self.df['close']
        self.df.loc[low, 'trend'] = -1

        high = (self.df['close'] > self.df['close_s1']) & (self.df['close'] > self.df['close_s2'])
        # high = self.df['close'] > self.df['close_s2']
        self.df.loc[high, 'close_l'] = self.df['close']
        self.df.loc[high, 'trend'] = 1


if len(sys.argv) > 1:
    fname = sys.argv[1]
    print('Reading local file {}'.format(fname))
    df = pd.read_csv(sys.argv[1])
else:
    symbol='HDFCLIFE'
    print('Downloading {} data from nsepy'.format(symbol))
    df = nsepy.get_history(
        symbol=symbol,
        start=dt.date(2017,1,1),
        end=dt.date(2018,1,19)
    )
    if df.empty:
        print('No data is received from nsepy. Exiting...')
        sys.exit()


df.reset_index(inplace=True)
df.columns = [i.lower() for i in df.columns]

lb = LineBreak(df)
lb.LINE_NUMBER = 2
data = lb.get_chart_data()
print(data.tail(38))
