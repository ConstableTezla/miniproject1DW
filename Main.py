# INF601 - Advanced Programming with Python
# Dalton Wright
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pprint

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
        closingList.append(round(price, 2))

    return closingList


# gets the closing price for Microsoft
msft = getClosing("MSFT")


stocks = ["MSFT", "APPL", "GME", "SONY", "META"]

# creates the array to plot Microsoft prices
msftClosing = np.array(getClosing("MSFT"))


plt.plot(msftClosing)
plt.xlabel('Days')
plt.ylabel('Closing Price')
plt.show()