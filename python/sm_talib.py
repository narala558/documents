from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
