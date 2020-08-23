from alpha_vantage.timeseries import Timeseries

key = '0656f4c261msh66918c48b22e843p1a7d6fjsn6b93574f99f2'

ts = Timeseries(key)

aapl, meta = ts.get.daily(symbol='AAPL')

print(aapl['2020-08-21'])