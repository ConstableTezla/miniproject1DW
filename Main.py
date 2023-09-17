# INF601 - Advanced Programming with Python
# Dalton Wright
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pprint
import copy

# Apple is AAPL
# Microsoft is MSFT
# Gamestop is GME
# Sony is SONY
# Facebook is META


def getClosing(ticker):
    # get the closing price for the last 10 trading days
    stock = yf.Ticker(ticker)

    # get historical market data
    hist = stock.history(period="10d")

    # create empty closing list for stock
    closingList = []

    # loop thorough closing prices and add to list
    for price in hist['Close']:
        closingList.append(price)

    return closingList


stocks = ["MSFT", "APPL", "GME", "SONY", "META"]

# gets the closing price for Microsoft
msft = getClosing("MSFT")

# creates the array to plot Microsoft prices
msftClosing = np.array(getClosing("MSFT"))

# allows the graph to start counting at 1 instead of 0
days = list(range(1, len(msftClosing)+1))

# get our min and max for y
prices = getClosing("MSFT")
prices.sort()
low_price = prices[0]
high_price = prices[-1]

# plots the graph
plt.plot(days, msftClosing)

# set our x axis min and max
# form (xmin, xmax, ymin, ymax)
plt.axis([1, 10, low_price-2, high_price+2])

# labels the graph
plt.xlabel('Days')
plt.ylabel('Closing Price')
plt.title('Closing Price for ' + "MSFT")

# prints the graph
plt.show()