"""
Homework 1: Financial Data Analysis 
Tasks 1-4: Loops, String Formatting, and stock data from Yahoo Finance
"""
 
# These imports are like getting all the ingredients and tools out before cooking.
# Nothing has been cooked yet, we are just stocking the kitchen.
 
# yfinance is our delivery runner. It is the only thing here that leaves the
# building. It goes out to Yahoo Finance, picks up the data, and brings it back.
import yfinance as yf
 
# pandas is our storage and prep system. It is the labeled containers and shelves
# that the delivery gets unpacked into. It gives us the DataFrame and Series
# objects that yfinance hands back, which is what makes history["Close"] and
# .head() work at all.
import pandas as pd
 
# numpy is our kitchen scale. It does pure math and nothing else. It does not go
# get anything and it does not organize anything. We use it to average the
# closing prices down in Task 4.
import numpy as np
 
# This is clearing off the counter. By default pandas hides some columns behind
# a "..." when a table is wide, the same way a cluttered counter hides things at
# the back. This says show me the whole spread.
pd.set_option('display.max_columns', None)
 
 
# Task 1: Looping and string formatting
# This part is just chopping. We have five garlic cloves sitting in a bowl
# (stock_prices), and the for loop picks up one clove at a time and does the
# exact same thing to each one before moving to the next.
#
# The loop variable "price" is just whichever clove is in our hand right now.
# It gets swapped out for the next one every time the loop comes back around.
#
# The f-string is the plating. A price is really just the number 90.5, but we
# don't serve a naked number. The ${price:.2f} is the garnish that forces two
# decimal places and a dollar sign so 90.5 shows up as $90.50 like real money.
 
print("Task 1: Formatted stock prices")
 
stock_prices = [120.50, 134.22, 150.10, 200.75, 90.50]
 
for price in stock_prices:
    print(f"Stock price: ${price:.2f}")
 
 
# Task 2: Fetching one year of Amazon data
# yf.Ticker("AMZN") is writing the order slip. Nothing has been delivered yet,
# we have only written "Amazon" down on a piece of paper. That is why this line
# runs instantly, because no data has actually moved.
#
# .history(period="1y") is the runner actually going to the market and coming
# back. This is the slow line in the whole script, because it is the only one
# that has to leave the kitchen and talk to the internet.
#
# What comes back is a full crate, not one item. It is about 250 rows (one per
# trading day) and each row has Open, High, Low, Close, and Volume.
#
# .head() is tasting a spoonful. We don't need to eat the whole pot to know what
# is in it, so we print the first 5 rows just to confirm the delivery showed up
# and looks right.
#
# The \n at the front of the print is just a blank line, so this section doesn't
# run right into the Task 1 output on screen.
 
print("\nTask 2: First 5 rows of AMZN, past year")
 
amazon = yf.Ticker("AMZN")
amzn_data = amazon.history(period="1y")
print(amzn_data.head())
 
 
# Task 3: Fetch 5 years of data for three stocks
# The assignment listed "FB", but Facebook renamed its ticker to META back in
# 2022, so "FB" doesn't return anything anymore. I swapped it out.
#
# This loop is doing the same errand three times: write the order slip, send the
# runner, unpack what comes back. Three separate trips, because each ticker is
# its own request out to Yahoo. That is also why this section takes a second.
#
# prices = {} is an empty fridge shelf. Then prices[symbol] = history["Close"]
# is us pulling just the one thing we actually want out of the crate, putting it
# in a container, and slapping a label on it that says GOOG.
#
# I used a dictionary here instead of a list on purpose. With a list I would
# have to remember that GOOG happened to be the first one I put in, and if I
# ever reordered the tickers my numbers would silently point at the wrong stock.
# A dictionary lets me just say prices['GOOG'] and get the right container back
# by name, no counting involved.
#
# history["Close"] pulls one single column out of the DataFrame, and what comes
# out is a Series. A Series is one labeled column that keeps its dates attached
# as the index. That is why .mean() works later without me telling it which
# column to look at, because there is only one.
#
# One note on the numbers themselves. .history() defaults to auto_adjust=True,
# so these prices arrive pre-washed and trimmed, meaning already adjusted for
# stock splits and dividends. That is the right ingredient for measuring how the
# investment actually performed over five years, but it does mean these numbers
# will not exactly match the price you see on a Yahoo Finance chart.
 
tickers = ["GOOG", "META", "AMZN"]
prices = {}
 
for symbol in tickers:
    stock = yf.Ticker(symbol)
    history = stock.history(period="5y")
    prices[symbol] = history["Close"]
 
# The instructions say to print the dictionary, but printing it straight would
# dump around 3,700 rows and bury every single thing after it. So instead I
# built a DataFrame out of the dictionary, which lines all three containers up
# on one tray side by side with the dates running down the left. Same data, just
# arranged so you can actually compare across it and see the keys are correct.
 
print("\nTask 3: Closing prices dictionary (as a combined table)")
 
closing_table = pd.DataFrame(prices)
print(closing_table.head())
 
# And here is each container on its own, first few rows only.
# .items() hands back both the label and what is inside it on each pass, which
# is why this loop has two variables instead of one.
 
for symbol, closing_prices in prices.items():
    print(f"\n{symbol} closing prices (first 5 of {len(closing_prices)} rows):")
    print(closing_prices.head())
 
 
# Task 4: Calculate the average closing price for each stock
# np.mean(closing_prices) is putting the container on the scale. It adds up
# every closing price in that Series and divides by how many there are.
#
# I print len(closing_prices) right next to the average to show my work. Five
# years is roughly 1,258 trading days, so if that count came back as 5 or as
# 12,000 I would know something went wrong with the fetch. The exact number will
# drift a little because "5y" is measured backward from whatever today is.
 
print("\nTask 4: Average closing prices over the past 5 years")
 
for symbol, closing_prices in prices.items():
    avg_price = np.mean(closing_prices)
    print(f"{symbol}: {len(closing_prices)} trading days, average: ${avg_price:.2f}")