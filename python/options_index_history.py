from datetime import date, datetime, timedelta

from nsepy import get_history
import matplotlib.pyplot as plt
from nsepy.derivatives import get_expiry_date


now = datetime.now()
today = now.date()
today = today + timedelta(days=30)


# options expire on last thursday of every month
p1_expiry = get_expiry_date(year=today.year, month=today.month - 1)
p2_expiry = get_expiry_date(
    year=today.year, month=today.month - 2) + timedelta(days=1)

print(p1_expiry, p2_expiry)

symbol = "NIFTY"
close = 'Close'

print(symbol)

df = get_history(
    symbol=symbol, index=True,
    strike_price=9600, option_type='CE',
    start=p2_expiry, end=p1_expiry, expiry_date=p1_expiry,
)
df = df.sort_index(ascending=True)
print(df[[close, 'Underlying']])

df = get_history(
    symbol=symbol, index=True,
    strike_price=10200, option_type='CE',
    start=p2_expiry, end=p1_expiry, expiry_date=p1_expiry,
)
df = df.sort_index(ascending=True)


def add_chgp(df, col, col_diff):
    df[col_diff] = round((1 - df[col] / df[col].shift(-1)) * 100, 2)
    df[col_diff] = df[col_diff].shift(1)


def add_diff(df, col, col_diff):
    df[col_diff] = df[col].shift(-1) - df[col]
    df[col_diff] = df[col_diff].shift(1)


close = 'Close'
close_diff = 'close_diff'
close_chgp = 'close_chgp'

underlying = 'Underlying'
underlying_diff = 'underlying_diff'
underlying_chgp = 'underlying_chgp'


add_diff(df, underlying, underlying_diff)
add_diff(df, close, close_diff)

# print(df.head())
# print(df[[close, close_diff, underlying, underlying_diff]])

# df[close_diff]
# fig, ax = plt.subplots()
# ax.plot(df.index, df[close_diff])
# ax.plot(df.index, df[underlying_diff])
# fig.set_size_inches(16, 8)

# plt.show()
