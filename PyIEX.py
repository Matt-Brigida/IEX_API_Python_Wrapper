import json
import requests

base_url = "https://api.iextrading.com/"
version = "1.0/"

def name(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["companyName"]
def exchange(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["exchange"]
def description(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["description"]
def industry(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["industry"]
def website(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["website"]
def CEO(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["CEO"]
def type(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["issueType"]
def sector(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["sector"]
def tags(ticker): return requests.get(base_url + version +"/stock/" + ticker + "/company").json()["tags"]

# JAMES, YOU DONT NEED TO TOUCH THIS ANYMORE. TRUST ME.
def sectorPerformance(sector=None):
	sectorDict = {}
	resp_str = requests.get(base_url + version + "/stock/market/sector-performance").json()
	if sector == None:
		return resp_str
	else:
		for i in resp_str:
			if i["name"] == sector:
				return i
			else:
				pass
# JAMES, YOU DONT NEED TO TOUCH THIS ANYMORE. TRUST ME.


def listTickers(sector=None):
		sectorDict = sectorPerformance(sector)
		if sector == None:
			tickerList = []
			for value in sectorDict:
				resp_str = requests.get(base_url + version + "/stock/market/collection/sector?collectionName=" + value["name"]).json()
				for y in resp_str:
					tickerList.append(y["symbol"])
			return tickerList
		else:
			tickerList = []
			resp_str = requests.get(base_url + version + "/stock/market/collection/sector?collectionName=" + sector).json()
			for y in resp_str:
				tickerList.append(y["symbol"])
			return tickerList
