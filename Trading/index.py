import pandas as pd
from key import api_key
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries

stock = input("What Stock Do You want?:")

print("")

def rsi_dataframe(stock=stock):
    api_key = 'api_key'
    period = 60
    ts = TimeSeries(key=api_key, output_format='pandas')
    data_ts = ts.get_intraday(stock.upper(), interval='1min', outputsize='full')

#indicator

    ti = TechIndicators(key='api_key', output_format='pandas')
    data_ti, meta_data_ti = ti.get_rsi(symbol=stock.upper(), interval='1min', time_period=period, series_type='close')

    df = data_ts

    return print(df)

rsi_dataframe()