# Descript: Send Crypto currency prices
# Import Libraries
from bs4 import BeautifulSoup
import requests
import time
import json

DOGE = 'DOGEUSDT'
BTC = 'BTCUSDT'

def get_ticker_price(ticker):
  # Curl ticker info
  url = "https://api.binance.com/api/v3/ticker/24hr?symbol="+ticker
  HTML = requests.get(url)
  soup = BeautifulSoup(HTML.text, 'html.parser')
  site_json = json.loads(soup.text)
  return site_json['askPrice']

def get_ticker_change(ticker):
  # Curl ticker info
  url = "https://api.binance.com/api/v3/ticker/24hr?symbol="+ticker
  HTML = requests.get(url)
  soup = BeautifulSoup(HTML.text, 'html.parser')
  site_json = json.loads(soup.text)
  return site_json['priceChangePercent']

  # Grab prices
def get_prices():
  oldtimeBTC = time.time()
  oldtimeDGE = time.time()
  # Create infinite loop to send/show price
  while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    # Get price
    BTCPrice = get_ticker_price(BTC)
    DOGEPrice = get_ticker_price(DOGE)
    # Check changes
    BTCChange = float(get_ticker_change(BTC))
    DOGEChange = float(get_ticker_change(DOGE))
    print("BTC: "+BTCPrice+" Change: "+str(BTCChange)+" DOGE: "+DOGEPrice+" Change: "+str(DOGEChange)+" at "+str(current_time))

get_prices()