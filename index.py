import os
import pandas as pd
from flask import Flask
from key import api_key
from flask_pymongo import PyMongo
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
if os.path.exists("env2.py"):
    import env2


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

stock = input("What Stock Do You want?:")

print("")

def rsi_dataframe(stock=stock):
    api_key = 'api_key'
    period = 60
    ts = TimeSeries(key=api_key, output_format='json')
    data_ts = ts.get_daily(stock.upper(), outputsize='compact')
    #print(f"DATA_TS: {data_ts}")
    #print(f"DATA: {type(data_ts[0])}")
    print(f"Date: {data_ts[1]['3. Last Refreshed']}")
    print(f"Open: {data_ts[0]['2020-10-21']['1. open']}")
    print(f"High: {data_ts[0]['2020-10-21']['2. high']}")
    print(f"Low: {data_ts[0]['2020-10-21']['3. low']}")
    print(f"Close: {data_ts[0]['2020-10-21']['4. close']}")
    print(f"Volume: {data_ts[0]['2020-10-21']['5. volume']}")

    ticker_ohlc = mongo.db.ohlc
    for ohlc in data_ts:
        ticker_ohlc.insert_one({
            "ticker": stock.upper(),
            "date": (f"{data_ts[1]['3. Last Refreshed']}"),
            "open": (f"{data_ts[0]['2020-10-21']['1. open']}"),
            "high": (f"{data_ts[0]['2020-10-21']['3. low']}"),
            "low": (f"{data_ts[0]['2020-10-21']['3. low']}"),
            "close": (f"{data_ts[0]['2020-10-21']['4. close']}"),
            "volume": (f"{data_ts[0]['2020-10-21']['5. volume']}")
        })

rsi_dataframe()