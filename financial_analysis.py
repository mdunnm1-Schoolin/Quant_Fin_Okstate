#These are like getting all the ingredients from the store before cooking. 
#This just gets data from Yahoo Finance
import yfinance as yf 
#This is what give us these pretty tables we see and makes history["Close"] and .mean() work
import pandas as pd
#We didn't call this directly but it does numerical computing
import numpy as np

pd.set_option('display.max_columns', None)

#Task 1: Looping and string formatting 
#This first area just lists the 5 made up prices and then prints them in the right format with 2 decimal places.

stock_prices = [120.50, 134.22, 150.10, 200.75, 90.50]

for price in stock_prices:
     print(f"Stock price: ${price:.2f}")

#Task 2: Fetch one year of Amazon data
#This area uses the yfinance library to fetch one year of Amazon stock data and prints the first 5 rows of the data. 

amazon = yf.Ticker("AMZN")
amzn_data = amazon.history(period="1y")
print(amzn_data.head())

#Task 3: Fetch 5 yrs of data for three stocks
#This shows and loops fecting five years of data for three different stocks and prints the closing prices for each stock.

tickers = ["GOOG", "META", "AMZN"]
prices = {}

for symbol in tickers:
     stock = yf.Ticker(symbol)
     history = stock.history(period="5y")
     prices[symbol] = history["Close"]

for symbol, closing_prices in prices.items():
     print(f"\n{symbol} closing prices:")
     print(closing_prices)

# Task 4: Calc the avg closing price for each stock 
#This area calculates the average closing price for each stock and prints it in the right format with 2 decimal places. 
#It takes 5 years of data for the average which is 1,254 trading days.

for symbol, closing_prices in prices.items():
     average = closing_prices.mean()
     print(f"{symbol} average closing price: ${average:.2f}")
