import sys
import numpy as np
import pandas as pd
import yfinance as yf
import time

def get_ticker_data(symbol):
    return yf.download(tickers=symbol, period="1d", interval="1m")

def generate_open_price(symbol):
    starttime = time.time()
    while True:
        data = get_ticker_data(symbol)
        current_open = data.iloc[[-1]]['Open']
        print(current_open)
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

def main():
    #symbol = input("Enter ticker name: ")
    symbol = "VEQT.TO"
    generate_open_price(symbol)

if __name__ == '__main__':
    main()

