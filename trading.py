import ccxt, yfinance
import pandas_ta as ta
import pandas as pd

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='1m', limit=500)
print(bars.type())

if __name__ == '__main__':
    pass