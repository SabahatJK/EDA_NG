'''
File with constants defined and few common functions

'''
import pandas as pd
from csv import reader
import os
import requests
import json
# import the Path function from pathlib
from pathlib import Path
import yfinance as yf
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import json
#hghjjhghghj


# Get data for a ticker from yFinance for last 10 years
# Input: 
#    ticker : the ticker to get data for
# Output: A data frame with date as index and Adj Close prices as the ticker name
def yfinance_tickers_data(ticker, start_date, end_date):
    
    
    ticker_data = yf.Ticker(ticker)
    df =ticker_data.history(start=start_date, end=end_date)
    df = df.drop(["Open", "High", "Low", "Volume", "Dividends", "Stock Splits" ], axis=1)
    return df
    # get ticker object
    #ticker = yf.Ticker(ticker)
    # get historical market data
    #df = ticker.history(start_date, end_date)
    #hist
    return df 

# Get data for a ticker from yFinance for last 10 years
# Input: 
#    ticker : the ticker to get data for
# Output: json object with data
def eia_consumption_data_by_series(api_key, series_id):

    # Create variable to hold request url
    api_url = f"http://api.eia.gov/series/?api_key={api_key}&series_id={series_id}"
    # Execute GET request and store response
    response_data = requests.get(api_url)
    # Formatting as json
    data = response_data.json()
    print(json.dumps(data, indent=4))
    return data    

def eia_category_info(api_key, category_id="480236"):

    # Create variable to hold request url
    api_url = f"http://api.eia.gov/category/?api_key={api_key}&category_id={category_id}"
    # Execute GET request and store response
    response_data = requests.get(api_url)
    # Formatting as json
    data = response_data.json()
    print(json.dumps(data, indent=4))
    return data    

def weather_data(file_path):
    weather_path = Path(file_path)
    weather_df = pd.read_csv(
    weather_path, index_col="Date", infer_datetime_format=True, parse_dates=True)
    weather_df = weather_df.sort_index()
    weather_df = weather_df.drop(["Departure", "HDD", "CDD", "Precipitation", "New Snow", "Snow Depth" ], axis=1)
    return weather_df






