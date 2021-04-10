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
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import panel as pn
from ipywidgets import interact
import ipywidgets as widgets
import plotly.express as px
from sklearn.linear_model import LinearRegression
pn.extension('plotly')
import hvplot.pandas

#ffdsfd
from bokeh.plotting import output_file, figure, show
from bokeh.models import LinearAxis, Range1d
from bokeh.models.renderers import GlyphRenderer

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
    
    return data    

def eia_consumption_data_by_series_df(api_key, series_id, state, stype, start_date, end_date, drop_date = True, include_state = False):
    
    data = eia_consumption_data_by_series(api_key, series_id);

    # create a data frame from the series of date and prices
    df_comsumption  = pd.DataFrame(list(data["series"][0]["data"]))

    str_state = f'{stype} Consumption'
    #Rename the columns from 0 & 1 to YearMonth and Consumption
    df_comsumption.rename(columns={0: "YearMonth", 1: str_state}, inplace = True)
    if include_state:
        df_comsumption["state"] = state 
    #Create a date column to select relevant data
    df_comsumption['DATE'] = pd.to_datetime(df_comsumption["YearMonth"], format="%Y%m")

    # Set datetype as datetime
    df_comsumption["DATE"].astype('datetime64', copy=False)

    # create mask to select only dates in our range
    mask = (df_comsumption['DATE'] >= start_date) & (df_comsumption['DATE'] <= end_date)

    # Apply mask and get relevant data 
    df_comsumption = df_comsumption.loc[mask]

    # Sort values 
    df_comsumption= df_comsumption.sort_values(by="DATE", ascending = True)

    # Set Index
    df_comsumption.set_index("YearMonth", inplace = True)
    if drop_date:
    # Drop date 
        df_comsumption.drop(columns="DATE", inplace = True)
    
    return df_comsumption


def eia_category_info(api_key, category_id="480236"):

    # Create variable to hold request url
    api_url = f"http://api.eia.gov/category/?api_key={api_key}&category_id={category_id}"
    # Execute GET request and store response
    response_data = requests.get(api_url)
    # Formatting as json
    data = response_data.json()
    print(json.dumps(data, indent=4))
    return data    

def weather_data(state, file_path):
    weather_path = Path(file_path)
    weather_df = pd.read_csv(
    weather_path, index_col="Date", infer_datetime_format=True, parse_dates=True)
    weather_df = weather_df.sort_index()
    weather_df = weather_df.drop(["Departure", "HDD", "CDD", "Precipitation", "New Snow", "Snow Depth" ], axis=1)
    #weather_df["state"] = state
    weather_df.rename(columns = {"Average": "Avg Temp"}, inplace = True)
    return weather_df

def agg_stock_closing_price_monthly(df_price):
    # Group by year and then month and get mean
    df_avg_price = df_price.groupby(by=[df_price.index.year, df_price.index.month]).mean()


    #rename the new multi index
    df_avg_price.index.rename("Year", level=0, inplace = True)
    df_avg_price.index.rename("Month", level=1, inplace = True)

    # Convert index to columns
    df_avg_price = pd.DataFrame(df_avg_price.to_records()) 


    # Add a 0 to months that are single digit
    df_avg_price["Month"] = df_avg_price.Month.map("{:02}".format)

    # Create a single new column to save the year and month
    df_avg_price['YearMonth'] = df_avg_price['Year'].apply(str) + df_avg_price['Month'].apply(str)


    # Create an Date column to convert all dates with the first day of the month
    df_avg_price['DATE'] = pd.to_datetime(df_avg_price["YearMonth"], format="%Y%m")

    # Set index to the YearMonth column
    df_avg_price = df_avg_price.set_index("YearMonth")

    # Drop the year and month Columns
    df_avg_price = df_avg_price.drop(["Year", "Month"], axis=1)

    #Verify data
    return df_avg_price


def agg_price_temperature_monthly(df_price_temp):
    # Group by year and then month and get mean
    df_avg_price_weather = df_price_temp.groupby(by=[df_price_temp.index.year, df_price_temp.index.month]).mean()


    #rename the new multi index
    df_avg_price_weather.index.rename("Year", level=0, inplace = True)
    df_avg_price_weather.index.rename("Month", level=1, inplace = True)

    # Convert index to columns
    df_avg_price_weather = pd.DataFrame(df_avg_price_weather.to_records()) 


    # Add a 0 to months that are single digit
    df_avg_price_weather["Month"] = df_avg_price_weather.Month.map("{:02}".format)

    # Create a single new column to save the year and month
    df_avg_price_weather['YearMonth'] = df_avg_price_weather['Year'].apply(str) + df_avg_price_weather['Month'].apply(str)


    # Create an Date column to convert all dates with the first day of the month
    df_avg_price_weather['DATE'] = pd.to_datetime(df_avg_price_weather["YearMonth"], format="%Y%m")

    # Set index to the YearMonth column
    df_avg_price_weather = df_avg_price_weather.set_index("YearMonth")

    # Drop the year and month Columns
    df_avg_price_weather = df_avg_price_weather.drop(["Year", "Month"], axis=1)

    #Verify data
    return df_avg_price_weather

def format_strorage_monthly(df_storage_data):
    # Group by year and then month and get mean
    df_storage_data_monthly = df_storage_data.groupby(by=[df_storage_data.index.year, df_storage_data.index.month]).mean()


    #rename the new multi index
    df_storage_data_monthly.index.rename("Year", level=0, inplace = True)
    df_storage_data_monthly.index.rename("Month", level=1, inplace = True)

    # Convert index to columns
    df_storage_data_monthly = pd.DataFrame(df_storage_data_monthly.to_records()) 


    # Add a 0 to months that are single digit
    df_storage_data_monthly["Month"] = df_storage_data_monthly.Month.map("{:02}".format)

    # Create a single new column to save the year and month
    df_storage_data_monthly['YearMonth'] = df_storage_data_monthly['Year'].apply(str) + df_storage_data_monthly['Month'].apply(str)


    # Create an Date column to convert all dates with the first day of the month
    df_storage_data_monthly['DATE'] = pd.to_datetime(df_storage_data_monthly["YearMonth"], format="%Y%m")

    # Set index to the YearMonth column
    df_storage_data_monthly = df_storage_data_monthly.set_index("YearMonth")

    # Drop the year and month Columns
    df_storage_data_monthly = df_storage_data_monthly.drop(["Year", "Month"], axis=1)

    #Verify data
    return df_storage_data_monthly


def agg_temperature_monthly(df_temp):
    # Group by year and then month and get mean
    df_avg_weather = df_temp.groupby(by=[df_temp.index.year, df_temp.index.month]).mean()


    #rename the new multi index
    df_avg_weather.index.rename("Year", level=0, inplace = True)
    df_avg_weather.index.rename("Month", level=1, inplace = True)

    # Convert index to columns
    df_avg_weather = pd.DataFrame(df_avg_weather.to_records()) 


    # Add a 0 to months that are single digit
    df_avg_weather["Month"] = df_avg_weather.Month.map("{:02}".format)

    # Create a single new column to save the year and month
    df_avg_weather['YearMonth'] = df_avg_weather['Year'].apply(str) + df_avg_weather['Month'].apply(str)


    # Create an Date column to convert all dates with the first day of the month
    df_avg_weather['DATE'] = pd.to_datetime(df_avg_weather["YearMonth"], format="%Y%m")

    # Set index to the YearMonth column
    df_avg_weather = df_avg_weather.set_index("YearMonth")

    # Drop the year and month Columns
    df_avg_weather = df_avg_weather.drop(["Year", "Month"], axis=1)

    #Verify data
    return df_avg_weather
    





