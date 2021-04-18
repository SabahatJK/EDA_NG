# Natural Gas Analysis
## Overview
Analysis of Natural Gas Stock Closing price with storage, consumption and temeprature.

The purpose of this project is to find the correlation between natural gas price and temperature. We initially start with the hope that there is a strong correlation between natural gas price and temperature. But the analysis we performed did not show the correlation we expected. We also compare natural gas prices with natural gas storage and natural gas consumption in the US. We found a strong correlation between temperature, NG storage, and NG consumption but no with NG price. 

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
- anaconda environment: A combination of the both dev and Pyviz (as installed in class). Clone dev environment and install Pyviz on it. It needs Pandas, Numpy, Alpaca, Yfinance, plotly go, requests, dotenv, json etc.


## Files:
- Natural_Gas_Analysis_and_Dashboard.ipynb : File that contains the Analysis and Dashboard code.
- helper.py : Python script with helper functions to help keep code clean and uncluttered.
- Third Party Files 
    - MCForecastTools.py : for the Monte Carlo Simulation

