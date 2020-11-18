import os
from flask import Flask
from flask_pymongo import PyMongo
from alpha_vantage.timeseries import TimeSeries
if os.path.exists("env2.py"):
    import env2

from datetime import datetime


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.api_key = os.environ.get("api_key")

mongo = PyMongo(app)

print("")
# Function for calling API and sending data to mongodb. 
# This has been imported to app.py as rsi and included in
# a python flask function /stock
def rsi_dataframe(stock):
    api_key = "api_key"

    stock = stock.upper()

    ticker_ohlc = mongo.db.ohlc
    today = datetime.utcnow().date()
    most_recent_stock_data = list(ticker_ohlc.find({"ticker": stock}).sort('-date').limit(1))
    # print(dir(most_recent_stock_data))
    most_recent_stock_data = most_recent_stock_data and most_recent_stock_data[0]
    print(most_recent_stock_data)
    if not most_recent_stock_data or most_recent_stock_data['date'] != str(today):
        ts = TimeSeries(key=api_key, output_format='json')
        data_ts = ts.get_daily(stock, outputsize='compact')
        # Allows date to align with API call
        previous_date = datetime.strptime(
            most_recent_stock_data['date'] if most_recent_stock_data else "2019-11-17",
            '%Y-%m-%d').date()

        print(previous_date)
        for ohlc_date, ohlc_data in data_ts[0].items():
            ohlc_date = datetime.strptime(ohlc_date, '%Y-%m-%d').date()
            if ohlc_date < previous_date:
                continue
            #inserts information received to mongodb
            ticker_ohlc.insert_one({
                "ticker": stock,
                "date": str(ohlc_date),
                "open": ohlc_data['1. open'],
                "high": ohlc_data['3. low'],
                "low": ohlc_data['3. low'],
                "close": ohlc_data['4. close'],
                "volume": ohlc_data['5. volume']
            })

    stock_data = ticker_ohlc.find({"ticker": stock}).sort('-date')
    return stock_data
