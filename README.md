# Natural Gas Analysis
## Overview
Analysis of Natural Gas Stock Closing price with storage, consumption and temeprature.

The purpose of this project was to determine if there's a relationship between temperature and the price of natural gas. We initially started with the hope of identifying a strong correlation between temperature and natural gas price. But the analysis we performed did not show the relationship we expected. We also analyzed natural gas storage and consumption to determine if temperature impacted either and if either had an impact on natural gas prices.  We found a strong relationship between temperature, NG storage, and NG consumption but no with NG price. We created a regression model that reasonably predicted residential natural gas consumption when using out of sample data.

## Prerequisites:
- Data Folder a folder where the analysis notebook file is located, contains the following data files:
    - Pittsburg_Area_Temp_2010-2014.csv and Pittsburg_Temp_2015_2019.csv
    - Hartford_Area_Temp_2010-2014.csv 
    - Chicago_Area_Temp_2010-2014.csv
    - Dallas_Area_Temp_2010-2014.csv
    - LosAngelus_Area_Temp_2010-2014.csv
    - NG_STOR_WKLY_S1_W.csv
- Dashbord_Text, a folder where the analysis file is located, contains the following overview text files:
    - Overview.txt: Overview of the Project
    - Closing_Price.txt: Overview of the storage analysis
    - Storage.txt: Overview of the Storage analysis
    - Consumption.txt: Overview of the Consumption analysis
    - Correlation.txt: Overview of the Correlation
    - Monte_Carlo.txt: Overview of the Monte_Carlo

- .env file located in the analysis notebook folder with EIA_API_KEY=<<EIA_API_KEY>> 
- Click the hyperlink to obtain your own [EIA_API_KEY](https://www.eia.gov/opendata/register.php) 
- anaconda environment: A combination of the both dev and Pyviz (as installed in class). Clone dev environment and install Pyviz on it. It needs Pandas, Numpy, Alpaca, Yfinance, plotly go, requests, dotenv, json etc.


## Files:
- Natural_Gas_Analysis_and_Dashboard.ipynb : File that contains the Analysis and Dashboard code.
- helper.py : Python script with helper functions to help keep code clean and uncluttered.
- Third Party Files 
    - MCForecastTools.py : for the Monte Carlo Simulation

