import os
from arctic import Arctic
from key import api_key
from flask_pymongo import PyMongo
from alpha_vantage.timeseries import TimeSeries
if os.path.exists("env.py"):
    import env

# Connect to Local MONGODB
store = Arctic('MONGO_URI')

# Create the library - defaults to VersionStore
store.initialize_library('Trading-data-set')

# Access the library
library = store['Trading-data-set']

api_key = 'api_key'
ts = TimeSeries(api_key, output_format='pandas')

fb_data, meta_data = ts.get_daily(symbol="FB", outputsize="full")
meta_data_fb = {'source': "Alpha Vantage"}

# Store the data in the library
library.write('Facebook', fb_data, metadata=meta_data_fb)

# Reading the data
item = library.read('Facebook')
FB = item.data
metadata = item.metadata

fb_data, meta_data = ts.get_daily(symbol="FB")