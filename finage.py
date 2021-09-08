import os
import requests

API_KEY = os.getenv("FINAGE_API_KEY")


def get_price(symbols):
    URL = "https://api.finage.co.uk/last/trade/stocks"
    return requests.get(URL, params={"symbols": ",".join(symbols), "apikey": API_KEY, "prepost": "true"}).json()


def get_finage_price(symbols):
    result = get_price(symbols)
    prices = {}

    for each in result:
        prices[each["symbol"]] = each["price"]

    return prices
