import pandas as pd
from key import api_key
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

stock = input("What Stock Do You want?:")

print("")

def rsi_dataframe(stock=stock):
    api_key = 'api_key'
    period = 60
    ts = TimeSeries(key=api_key, output_format='pandas')
    data_ts = ts.get_daily(stock.upper(), outputsize='full')

    df = data_ts[0],[period]

    return print(df)

rsi_dataframe()