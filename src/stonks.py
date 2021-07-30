import sys
import time
import numpy as np
import pandas as pd
import yfinance as yf
import subprocess as sp
from datetime import datetime, date

# get stock data from yahoo finance
def get_ticker_data(symbol):
    return yf.download(tickers=symbol, period="1d", interval="1m")

# generate market price every minute
def generate_open_price(symbol, notify_price):
    starttime = time.time()
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        today = date.today()
        current_date = today.strftime("%b-%d-%Y")
        data = get_ticker_data(symbol)
        current_open = data.iloc[[-1]]['Open']

        open_price = round(current_open[0], 2)
        print(symbol + " @ " + current_time + " (" + current_date + ")")
        print(open_price)
        print("\n")
        if (open_price > notify_price):
            # change the signs when done testing
            notify()

        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

# set notification when price goes below threshold
def notify():
    sp.call(["notify-send", "Title", "some text"])
    return

def main():
    #symbol = input("Enter ticker name: ")
    symbol = "VEQT.TO"
    #min_open = input("Enter min. price for notification: ")
    min_open = 35.15
    generate_open_price(symbol, min_open)

if __name__ == '__main__':
    main()
