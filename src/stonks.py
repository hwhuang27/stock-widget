import sys
import time
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime

# get stock data from yahoo finance
def get_ticker_data(symbol):
    return yf.download(tickers=symbol, period="1d", interval="1m")

# generate market price every minute
def generate_open_price(symbol, notify_price):
    starttime = time.time()
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        data = get_ticker_data(symbol)
        current_open = data.iloc[[-1]]['Open']

        open_price = round(current_open[0], 2)
        print(symbol + " @ " + current_time)
        print(open_price)

        if (open_price <= notify_price):
            notify()


        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

# set notification when price goes below threshold
def notify():
    # notification code here
    


    print("BUY NOW!!!") # placeholder
    return

def main():
    #symbol = input("Enter ticker name: ")
    symbol = "VEQT.TO"
    #min_open = input("Enter min. price for notification: ")
    min_open = 35.15
    generate_open_price(symbol, min_open)

if __name__ == '__main__':
    main()
