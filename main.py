import os
import csv
import time

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


header = ["timestamp", "twelvedata", "finage", "yahoo_finance"]

print("start")

twelvedata_prices = get_twelvedata_price(SYMBOLS)
# print(twelvedata_prices)

finage_prices = get_finage_price((SYMBOLS))
# print(finage_prices)

yfinance_prices = get_yfinance_prices(SYMBOLS)
# print(yfinance_prices)

for symbol in SYMBOLS:
    with open("./reports/" + symbol + ".csv", "a+", encoding="UTF8") as f:
        writer = csv.writer(f)

        # write the header
        # writer.writerow(header)

        # write the data
        data = [int(time.time()), twelvedata_prices[symbol], finage_prices[symbol], yfinance_prices[symbol]]
        writer.writerow(data)
