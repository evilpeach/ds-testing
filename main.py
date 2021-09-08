import os
import csv

from twelvedata import get_twelvedata_price
from yahoo_finance import get_yfinance_prices
from finage import get_finage_price

SYMBOLS = [
    "AAPL",
    "GOOGL",
    "TSLA",
    "NFLX",
    "QQQ",
    "TWTR",
    "BABA",
    "IAU",
    "SLV",
    "USO",
    "VIXY",
    "AMZN",
    "MSFT",
    "FB",
    "GS",
    "ABNB",
    "GME",
    "AMC",
    "SPY",
    "COIN",
    "ARKK",
    "SQ",
    "AMD",
    "HOOD",
]


header = ["timestamp", "twelvedata"]

print("start")

twelvedata_prices = get_twelvedata_price(SYMBOLS)
print(twelvedata_prices)

yfinance_prices = get_yfinance_prices(SYMBOLS)
print(yfinance_prices)

finage_prices = get_finage_price((SYMBOLS))
print(finage_prices)
