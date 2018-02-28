import collections
import os
import time
import datetime as dt
from os.path import join
import warnings
import sys

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 2000)

warnings.simplefilter(action='ignore', category=FutureWarning)

try:
    df = pd.read_csv(sys.argv[1])
except:
    df = pd.read_csv('SBIN')


df.set_index('Date', inplace=True)
df.sort_index(ascending=True, inplace=True)


uu_columns = [
    'Symbol', 'Series', 'Volume', 'Turnover',
    'Last', 'VWAP', 'Trades', 'Deliverable Volume', '%Deliverble'
]
df.drop(uu_columns, axis=1, inplace=True)

# print(df.columns)

df['open'] = df.pop('Open')
df['high'] = df.pop('High')
df['low'] = df.pop('Low')
df['close'] = df.pop('Close')
df['close_s1'] = df.pop('Prev Close')

brick_size = 2


df['open_r'] = (df['close_s1'] // brick_size) * brick_size
df['high_r'] = (df['high'] // brick_size) * brick_size
df['low_r'] = (df['low'] // brick_size) * brick_size
df['close_r'] = (df['close'] // brick_size) * brick_size
df['close_r_s1'] = (df['close_s1'] // brick_size) * brick_size


# df['high_ra'] = df['high'].apply()


df['cr_diff'] = df['close_r'] - df['close_r'].shift()
df = df[df['cr_diff'] != 0]
df['bricks'] = df.loc[:, ('cr_diff', )] / brick_size
# df['b_csum'] = df['bricks'].cumsum()
# df.loc[:, ('bricks', )] = df['bricks'].astype(int)

df['bricks_s1'] = df['bricks'].shift()
df['tc'] = np.where((df['bricks'] * df['bricks_s1']) < 0, True, False)

df.pop('Unnamed: 0')
print(df.head())

while True:
    df['cr_diff'] = df['close_r'] - df['close_r'].shift()
    df = df[df['cr_diff'] != 0]
    df['bricks'] = df.loc[:, ('cr_diff', )] / brick_size

    df['bricks_s1'] = df['bricks'].shift()
    df['tc'] = np.where((df['bricks'] * df['bricks_s1']) < 0, True, False)
    filtered_df = df[(~df['tc']) | ~(abs(df['bricks']) == 1)]
    if len(df) == len(filtered_df):
        break
    df = filtered_df

print('done')


# df = df[(abs(df['bricks']) != 1)]
# df['bl'] = abs(df['bricks'])
# df['bs'] = df['bricks'] > 0

bricks = df['bricks']
n_bricks = []
prev_sign = False

for brick in bricks:
    current_sign = brick > 0
    if prev_sign != current_sign:
        tc = True
        rs = 2


# df['bl'].apply() - 2 if df['tc']
uu_columns = ['open', 'high', 'low', 'close']
df.drop(uu_columns, axis=1, inplace=True)

asign = np.sign(bricks)
df['rtc'] = ((np.roll(asign, 1) - asign) != 0).astype(int)

df['u_bricks'] = df['bricks'][df['rtc'] == 1]
df['u_bricks'] = df['u_bricks'].apply(lambda x: x - 2 if x > 0 else x + 2)
df['u_bricks'][df['rtc'] == 0] = df['bricks']

column = 'bricks'
bricks = df[column]
grouper = (bricks != bricks.shift()).cumsum()
df['r_csum'] = df.groupby(grouper)[column].cumsum()
df['rdiff'] = df[column].diff()

# df = df[df['bricks'] != 0]
# df = df['bricks']

# rscore = df['rcsum'][df['rdiff'].shift(-1) != 0]
# bricks = df[df['bricks'] != 0]['bricks'].values

print(df.head(10))
# print(df.tail(100))
print(df.tail(20))
df = df[['close_r', 'u_bricks']]
df = df[df['u_bricks'] != 0]

df.reset_index(inplace=True)
df.dropna(inplace=True)
df['date'] = df.pop('Date')
print(df.head(10))
print(df.tail(10))

columns = ['open', 'close', 'date']
df2 = pd.DataFrame(
    columns=columns,
    data=[[0, 0, 0]],
)

prev_bricks = -1

cls = 196

for index, row in df.iterrows():
    # cls = row['close_r']
    bricks = row['u_bricks']
    date = row['date']

    data = []
    for i in range(int(abs(bricks))):
        if prev_bricks * bricks < 0 and i == 0 :
            cls = cls + brick_size * (bricks / abs(bricks))

        r = [
            cls,
            cls + (brick_size * (bricks / abs(bricks))),
            date
        ]
        data.append(r)

        cls = r[1]
        prev_bricks = bricks

    # print(data)
    sdf = pd.DataFrame(data=data, columns=columns)
    # print(df2)
    # print(sdf)

    df2 = pd.concat([df2, sdf])


df2.to_csv('renko.csv')
print(df2.tail(20))


class Renko:

    PERIOD_CLOSE = 1
    PRICE_MOVEMENT = 2

    brick_size = 1
    chart_type = PERIOD_CLOSE

    required_columns = {'open', 'high', 'low', 'close'}

    def __init__(df):
        self.df = df
        self._validate_df()
        self.rdf = df
        self.bdf = None

    def _validate_df(self):
        if required_columns not in set(self.df.columns):
            raise 'DataFrame should have OHLC data'

    def get_bricks(self):
        if chart_type == PERIOD_CLOSE:
            self.period_close_bricks()
        else:
            self.price_movement_bricks()

        return self.bdf

    def period_close_bricks(self):
        brick_size = self.brick_size
        df = self.rdf

        df['open_r'] = (df['close_s1'] // brick_size) * brick_size
        df['high_r'] = (df['high'] // brick_size) * brick_size
        df['low_r'] = (df['low'] // brick_size) * brick_size
        df['close_r'] = (df['close'] // brick_size) * brick_size
        df['close_r_s1'] = (df['close_s1'] // brick_size) * brick_size
        self.filter_noise()

        bricks = df['bricks']
        asign = np.sign(bricks)
        df['rtc'] = ((np.roll(asign, 1) - asign) != 0).astype(int)

        df['u_bricks'] = df['bricks'][df['rtc'] == 1]
        df['u_bricks'] = df['u_bricks'].apply(lambda x: x - brick_size if x > 0 else x + brick_size)
        df['u_bricks'][df['rtc'] == 0] = df['bricks']

        df = df[['close_r', 'u_bricks']]
        df = df[df['u_bricks'] != 0]
        df.reset_index(inplace=True)
        df.dropna(inplace=True)
        self.calculate_bricks_from_diff()


    def calculate_bricks_from_diff(self):
        columns = ['open', 'close', 'date']
        self.bdf = pd.DataFrame(
            columns=columns,
            data=[[0, 0, 0]],
        )

        prev_bricks = -1
        cls = self.rdf['close'].iloc[0]

        for index, row in self.rdf.iterrows():
            bricks = row['u_bricks']
            date = row['date']

            data = []

            for i in range(int(abs(bricks))):
                if prev_bricks * bricks < 0 and i == 0 :
                    cls = cls + brick_size * (bricks / abs(bricks))

                r = [
                    cls,
                    cls + (brick_size * (bricks / abs(bricks))),
                    date
                ]
                data.append(r)

                cls = r[1]
                prev_bricks = bricks

            # print(data)
            sdf = pd.DataFrame(data=data, columns=columns)

            bdf = pd.concat([df2, sdf])

        return bdf


    def filter_noise(self):
        df = self.rdf

        df['cr_diff'] = df['close_r'] - df['close_r'].shift()
        df = df[df['cr_diff'] != 0]
        df['bricks'] = df.loc[:, ('cr_diff', )] / brick_size
        df['bricks_s1'] = df['bricks'].shift()
        df['tc'] = np.where((df['bricks'] * df['bricks_s1']) < 0, True, False)


        while True:
            df['cr_diff'] = df['close_r'] - df['close_r'].shift()
            df = df[df['cr_diff'] != 0]
            df['bricks'] = df.loc[:, ('cr_diff', )] / brick_size

            df['bricks_s1'] = df['bricks'].shift()
            df['tc'] = np.where((df['bricks'] * df['bricks_s1']) < 0, True, False)
            filtered_df = df[(~df['tc']) | ~(abs(df['bricks']) == 1)]
            if len(df) == len(filtered_df):
                break
            df = filtered_df


        self.rdf = df



"""
Usage:

renko = Renko(df)
renko.brick_size = 2
renko.get_bricks()
"""
