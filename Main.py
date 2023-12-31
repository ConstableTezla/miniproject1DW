# INF601 - Advanced Programming with Python
# Dalton Wright
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

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


def printGraph(stock):

    # creates the array to plot stock prices
    stockClosing = np.array(getClosing(stock))

    # allows the graph to start counting at 1 instead of 0
    days = list(range(1, len(stockClosing) + 1))

    # get our min and max for y
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # plots the graph
    plt.plot(days, stockClosing)

    # set our x axis min and max
    # form (xmin, xmax, ymin, ymax)
    plt.axis([1, 10, low_price - 2, high_price + 2])

    # labels the graph
    plt.xlabel('Days')
    plt.ylabel('Closing Price')
    plt.title('Closing Price for ' + stock)

    # names and saves charts as a png file
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    # prints the graph
    plt.show()


def getStocks():

    stocks = []

    print("Please enter 5 stocks to graph:")
    for i in range(1, 6):

        while True:
            print("Enter stock ticker number " + str(i))
            ticker = input("> ")
            try:
                print("Checking Ticker")
                stock = yf.Ticker(ticker)
                stock.info
                stocks.append(ticker)
                print("Valid Ticker")
                break
            except:
                print("This is not a valid stock. Please enter another.")

    return stocks


# Start of program

# create our charts folder
try:
    Path("Charts").mkdir()
except FileExistsError:
    pass

for stock in getStocks():
    getClosing(stock)
    printGraph(stock)