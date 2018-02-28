import os
import datetime as dt
from datetime import datetime

import btstrategies

import backtrader as bt
import pandas as pd


class SmaCross(bt.SignalStrategy):
    params = (('pfast', 10), ('pslow', 30),)

    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))


class SupertrendCross(bt.SignalStrategy):
    params = ()

    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))


class RenkoCross(bt.SignalStrategy):

    params = ()

    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))


cerebro = bt.Cerebro()
cerebro.broker.setcash(1000000.00)

fname = os.path.expanduser('~/.stocks/RELIANCE')
nfname = os.path.expanduser('~/.stocks/backtrader/RELIANCE')

df = pd.read_csv(fname)
ndf = df[['Date', 'High', 'Low', 'Open', 'Close', 'Volume']]
ndf.to_csv(nfname, index=False)


data = bt.feeds.GenericCSVData(
    dataname=nfname,
    fromdate=dt.datetime(2017, 1, 1),
    # todate=datetime.datetime(2000, 12, 31),
    nullvalue=0.0,
    dtformat=('%Y-%m-%d'),
    datetime=0,
    high=1,
    low=2,
    open=3,
    close=4,
    volume=5,
    openinterest=-1
)
cerebro.adddata(data)

# cerebro.addstrategy(SmaCross)
cerebro.addstrategy(btstrategies.BBandsStrategy)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
# cerebro.plot()
