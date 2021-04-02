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

# Get data for a ticker from yFinance
# Input: 
#    ticker : the ticker to get data for
#    start : from start date 
#    end: to end date
# Output: A data frame with date as index and Adj Close prices as the ticker name
def yfinance_tickers_data_by_dates(tickers, start, end):
    df = yf.download(tickers, start=start_date, end=end_date)
    # Drop extra columns
    #df.drop( columns= ["Open", "High", "Low", "Close", "Volume"], inplace = True)
    # Rename the Close Column to Goog
    #df.rename(columns={"Adj Close": tickers}, inplace = True)
    return df 

# Get data for a ticker from yFinance for last 10 years
# Input: 
#    ticker : the ticker to get data for
# Output: A data frame with date as index and Adj Close prices as the ticker name
def yfinance_tickers_data(ticker):
    # get ticker object
    ticker = yf.Ticker(ticker)
    # get historical market data
    df = ticker.history(period="max")
    #hist
    return df 

# Get data for a ticker from yFinance for last 10 years
# Input: 
#    ticker : the ticker to get data for
# Output: json object with data
def eia_consumption_data_by_series(api_key, series_id="NG.NA1490_STX_2.A"):

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



