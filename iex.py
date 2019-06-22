### Functions to interact with the IEX API:  https://iextrading.com/developer/docs/

import json
import requests
import pandas as pd

base_url = "https://api.iextrading.com/"
version = "1.0/"

# r = requests.get(base_url + version + "/stock/etp/company")

r = requests.get(base_url + version + "/stock/etp/volume-by-venue")

json_data = r.json()

# json_data["companyName"]
# json_data["exchange"]
# json_data["description"]
# json_data["issueType"]

pd.DataFrame.from_dict(json_data)

# pd.DataFrame([json_data], columns=json_data.keys())


def ven(ticker):
    """Get volume-by-venue for ticker"""
    tmp = pd.DataFrame.from_dict(requests.get(base_url + version + "/stock/" + ticker + "/volume-by-venue").json())
    tmp["Ticker"] = ticker
    return tmp

def one_day(ticker):
    """Get 1 minute data for the last day""" 
    tmp = pd.DataFrame.from_dict(requests.get(base_url + version + "/stock/" + ticker + "/chart/1d").json())
    tmp["Ticker"] = ticker
    return tmp

def symbols_list():
    tmp = pd.DataFrame.from_dict(requests.get(base_url + version + "/ref-data/symbols").json())
    return tmp

sym = symbols_list()
## then can get a list of tickers via sym["symbols"]

def book(ticker):
    tmp = pd.DataFrame.from_dict(requests.get(base_url + version + "/deep?symbols=" + ticker).json())
    return tmp
