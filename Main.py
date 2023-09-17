# INF601 - Advanced Programming with Python
# Dalton Wright
# Mini Project 1

import yfinance as yf
import pprint

# Apple is AAPL
# Microsoft is MSFT

def getClosing(ticker):
    stock = yf.Ticker("ticker")

    # get historical market data
    hist = stock.history(period="10d")

    # create empty closing list for stock
    closing_list = []

    # loop thorough closing prices and add to list
    for price in hist['Close']:
        closing_list.append(price)

    return closing_list

msft = getClosing('MSFT')

print('msft')