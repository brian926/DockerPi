# Descript: Send Crypto currency prices
from bs4 import BeautifulSoup
import requests
import time
import json
import mysql.connector

# Check connection to the db, sleep if db isn't up
def check_db():
  connection = False
  while connection==False:
    try:
      mydb = mysql.connector.connect(
        host="mysqldb",
        user="PyU",
        password="PyP",
      )
      print("Database is up")
      connection=True
      mydb.close()
    except mysql.connector.Error as err:
      print(err)
      pass
    time.sleep(30)

# Create tables in the db
def create_tables():
  try:
    mydb = mysql.connector.connect(
      host="mysqldb",
      user="PyU",
      password="PyP",
      database="crypto"
    )
    print("Connected to database")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS Bitcoin")
  sql ='''CREATE TABLE Bitcoin(
  PRICE FLOAT,
  TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  )'''
  cursor.execute(sql)
  print("created Bitcoin table")

  
  cursor.execute("DROP TABLE IF EXISTS Dogecoin")
  sql ='''CREATe TABLE Dogecoin(
    PRICE FLOAT,
    TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  )'''
  cursor.execute(sql)

  mydb.close()

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

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="PyU",
    password="PyP",
    database="crypto"
  )
  cursor = mydb.cursor()
  # Create infinite loop to send/show price
  while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    sql_time = time.strftime('%Y-%m-%d %H:%M:%S')
    # Get price
    BTCPrice = get_ticker_price(BTC)
    DOGEPrice = get_ticker_price(DOGE)
    # Check changes
    BTCChange = float(get_ticker_change(BTC))
    DOGEChange = float(get_ticker_change(DOGE))
    # print("BTC: "+BTCPrice+" Change: "+str(BTCChange)+" DOGE: "+DOGEPrice+" Change: "+str(DOGEChange)+" at "+str(current_time))

    sql_b = "INSERT INTO Bitcoin (price, time) VALUES (%s, %s)"
    val_b = (BTCPrice, sql_time)

    sql_d = "INSERT INTO Dogecoin (price, time) VALUES (%s, %s)"
    val_d = (DOGEPrice, sql_time)

    try:
      cursor.execute(sql_b, val_b)
      print("Inserted {} at {}".format(BTCPrice, sql_time))
    except mysql.connector.Error as err:
      print("Something went wrong : {}".format(err))
      raise
    
    try:
      cursor.execute(sql_d, val_d)
      print("Inserted {} at {}".format(DOGEPrice, sql_time))
    except mysql.connector.Error as err:
      print("Something went wrong : {}".format(err))
      raise

    time.sleep(60)

check_db()
create_tables()
get_prices()