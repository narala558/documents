import os
import sys
import time
import datetime as dt

import quandl
import numpy as np
import pandas as pd
import nsepy


class PnF:

    TREND_CHANGE_DIFF = 2

    box_size = 1

    required_columns = {'open', 'high', 'low', 'close'}

    def __init__(self, df):
        self.odf = df
        self.df = df
        self._validate_df()
        self.bdf = None

    def _validate_df(self):
        if not self.required_columns.issubset(self.df.columns):
            raise ValueError('DataFrame should have OHLC {} columns'.format(self.required_columns))

    def get_chart_data(self):
        box_size = self.box_size
        self.df = self.df[['date', 'close']]

        self.df.loc[:, 'close_s1'] = self.df['close'] - self.df['close'].shift()
        self.df.dropna(inplace=True)

        self.df.loc[:, 'close_r'] = (self.df['close'] // self.box_size) * self.box_size
        self.df.loc[:, 'close_r_s1'] = (self.df['close_s1'] // self.box_size) * self.box_size

        if debug:
            print(self.df.head())

        self.filter_noise()

        bricks = self.df['bricks']
        asign = np.sign(bricks)
        self.df.loc[:, 'rtc'] = ((np.roll(asign, 1) - asign) != 0).astype(int)

        self.df.loc[:, 'u_bricks'] = self.df.loc[self.df['rtc'] == 1, 'bricks']
        self.df.loc[:, 'u_bricks'] = self.df['u_bricks'].apply(
            lambda x: x - self.TREND_CHANGE_DIFF if x > 0 else x + self.TREND_CHANGE_DIFF
        )
        self.df.loc[self.df['rtc'] == 0, 'u_bricks'] = self.df['bricks']

        self.df = self.df[['close_r', 'u_bricks', 'date']]
        self.df = self.df[self.df['u_bricks'] != 0]
        self.df.reset_index(inplace=True)
        self.df.dropna(inplace=True)

        self.calculate_bricks_from_diff()
        self.shift_bricks()

        self.bdf.reset_index(inplace=True, drop=True)

        return self.bdf

    def shift_bricks(self):
        shift = self.odf['close'].iloc[-1] - self.bdf['close'].iloc[-1]
        if abs(shift) < self.box_size:
            return
        step = shift // self.box_size
        self.bdf[['open', 'close']] += step * self.box_size

    def calculate_bricks_from_diff(self):
        box_size = self.box_size

        columns = ['open', 'close', 'date']
        self.bdf = pd.DataFrame(
            columns=columns,
            data=[[0, 0, 0]],
        )

        prev_bricks = 1

        cls = (self.odf['close'].iloc[0] // box_size) * box_size

        for index, row in self.df.iterrows():
            bricks = row['u_bricks']
            date = row['date']

            data = []

            for i in range(int(abs(bricks))):
                if prev_bricks * bricks < 0 and i == 0 :
                    cls = cls + box_size * (bricks / abs(bricks))

                r = [
                    cls,
                    cls + (box_size * (bricks / abs(bricks))),
                    date
                ]
                data.append(r)

                cls = r[1]
                prev_bricks = bricks

            # print(data)
            sdf = pd.DataFrame(data=data, columns=columns)

            self.bdf = pd.concat([self.bdf, sdf])

        return self.bdf


    def filter_noise(self):
        df = self.df
        box_size = self.box_size

        df.loc[:, 'cr_diff'] = df['close_r'] - df['close_r'].shift()
        df = df[df['cr_diff'] != 0]
        df.loc[:, 'bricks'] = df.loc[:, ('cr_diff', )] / box_size
        df.loc[:, 'bricks_s1'] = df['bricks'].shift()
        df.loc[:, 'tc'] = np.where((df['bricks'] * df['bricks_s1']) < 0, True, False)


        while True:
            df.loc[:, 'cr_diff'] = df['close_r'] - df['close_r'].shift()
            df = df[df['cr_diff'] != 0]

            df['bricks'] = df.loc[:, ('cr_diff', )] / box_size
            df['bricks_s1'] = df['bricks'].shift()
            df['tc'] = np.where((df['bricks'] * df['bricks_s1']) < 0, True, False)

            filtered_df = df[(~df['tc']) | ~(abs(df['bricks']) == 1)]
            if len(df) == len(filtered_df):
                break
            df = filtered_df


        self.df = df


def stock_df(symbol):
    file = '{}'.format(symbol.upper())
    if not os.path.exists(file):
        print('Downloading {}'.format(symbol))
        time.sleep(5)
        quandl.ApiConfig.api_version = '2015-04-09'
        df = quandl.get('NSE/{}'.format(symbol), start_date='2017-01-01', end_date='2018-01-25')
        df.reset_index(inplace=True)
        df.columns = [i.lower() for i in df.columns]
        df.to_csv(file)
    return pd.read_csv(file)


if len(sys.argv) > 1:
    fname = sys.argv[1]
    print('Reading local file {}'.format(fname))
    df = pd.read_csv(sys.argv[1])
else:
    symbol='SBIN'
    # print('Downloading {} data from nsepy'.format(symbol))
    # df = nsepy.get_history(
    #     symbol=symbol,
    #     start=dt.date(2017,1,1),
    #     end=dt.date(2018,1,19)
    # )
    # if df.empty:
        # print('No data is received from nsepy.')
        # sys.exit()
    df = stock_df(symbol)

debug = True
df.reset_index(inplace=True)
df.columns = [i.lower() for i in df.columns]
print(df.tail(20))

pnf = PnF(df)
pnf.box_size = 2
data = pnf.get_chart_data()
print(data.tail(20))
