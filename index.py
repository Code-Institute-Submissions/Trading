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
    ts = TimeSeries(key=api_key, output_format='pandas')
    data_ts = ts.get_daily(stock.upper(), outputsize='full')

    df = data_ts[0],[period]

    ticker_ohlc = mongo.db.ohlc
    for ohlc in df:
        ticker_ohlc.insert_one({
            "ticker": stock.upper(),
            "date": "",
            "open": "",
            "high": "",
        })

    return print(df)

rsi_dataframe()