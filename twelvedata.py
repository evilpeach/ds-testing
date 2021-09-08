import os
import requests
import time


API_KEY = os.getenv("TWELVEDATA_API_KEY")


def get_price(symbols):
    URL = "https://api.twelvedata.com/price"
    return requests.get(URL, params={"symbol": ",".join(symbols), "apikey": API_KEY, "prepost": "true"}).json()


def get_twelvedata_price(symbols):
    result = get_price(symbols)
    prices = {}

    for symbol in result:
        prices[symbol] = result[symbol]["price"]

    return prices