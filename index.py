import os
from flask import Flask
from key import api_key
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

# stock = input("What Stock Do You want?:")

print("")

def rsi_dataframe(stock):
    api_key = 'api_key'
    period = 60

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

        previous_date = datetime.strptime(
            most_recent_stock_data['date'] if most_recent_stock_data else "2019-10-31",
            '%Y-%m-%d').date()

        print(previous_date)
        for ohlc_date, ohlc_data in data_ts[0].items():
            ohlc_date = datetime.strptime(ohlc_date, '%Y-%m-%d').date()
            if ohlc_date < previous_date:
                continue

            ticker_ohlc.insert_one({
                "ticker": stock,
                "date": str(ohlc_date),
                "open": ohlc_data['1. open'],
                "high": ohlc_data['3. low'],
                "low": ohlc_data['3. low'],
                "close": ohlc_data['4. close'],
                "volume": ohlc_data['5. volume']
            })


        # for ohlc in data_ts[0]:
        #     if ohlc[]
        #     ticker_ohlc.insert_one({
        #         "ticker": stock.upper(),
        #         "date": (f"{data_ts[1]['3. Last Refreshed']}"),
        #         "open": (f"{data_ts[0]['2020-10-27']['1. open']}"),
        #         "high": (f"{data_ts[0]['2020-10-27']['3. low']}"),
        #         "low": (f"{data_ts[0]['2020-10-27']['3. low']}"),
        #         "close": (f"{data_ts[0]['2020-10-27']['4. close']}"),
        #         "volume": (f"{data_ts[0]['2020-10-27']['5. volume']}")
        #     })

    stock_data = ticker_ohlc.find({"ticker": stock}).sort('-date')
    return stock_data


    #print(f"DATA_TS: {data_ts}")
    #print(f"DATA: {type(data_ts[0])}")
    # print(f"Date: {data_ts[1]['3. Last Refreshed']}")
    # print(f"Open: {data_ts[0]['2020-10-27']['1. open']}")
    # print(f"High: {data_ts[0]['2020-10-27']['2. high']}")
    # print(f"Low: {data_ts[0]['2020-10-27']['3. low']}")
    # print(f"Close: {data_ts[0]['2020-10-27']['4. close']}")
    # print(f"Volume: {data_ts[0]['2020-10-27']['5. volume']}")


# rsi_dataframe()