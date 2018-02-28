import os
import time

import requests
import pandas as pd
import techind


stocks_dir = os.path.expanduser('~/.stocks')


def supertrend(df, symbol=None):
    stxd = 'STXD_7_3'
    if stxd not in df.columns:
        if not symbol:
            symbol = df.iloc[0]['Symbol']
        print('Calculating stx for {}'.format(symbol))
        df = techind.SuperTrend(df, 15, 3)
        df[stxd] = df['STX_7_3'].diff()

    return df


host = 'https://kitecharts.zerodha.com'
endpoint = host + '/api/chart/5332481/15minute'
endpoint = host + '/api/chart/738561/day'

stocks = {
    'RELIANCE': '738561',
    'ICICIBANK': '1270529',
    'DRREDDY': '225537',
}


def get_kite_df(symbol, params, cache=True):
    file = os.path.join(stocks_dir, 'kite', symbol.upper())
    if not cache:
        try:
            os.remove(file)
        except:
            pass

    if not os.path.exists(file):
        print('Downloading {}'.format(symbol))
        time.sleep(5)

        duration = '15minute'
        stock = stocks[symbol.upper()]
        endpoint = host + '/api/chart/{}/{}'.format(stock, duration)
        response = requests.get(endpoint, params=params)
        print(response.url)
        try:
            j = response.json()
            data = j['data']['candles']
            df = pd.DataFrame(data)
        except:
            print(response.text)

        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        df.set_index('Date', inplace=True)
        df.to_csv(file)
    return pd.read_csv(file)
