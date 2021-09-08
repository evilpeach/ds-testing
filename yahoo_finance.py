import datetime
import concurrent.futures
import yfinance as yf
import sys


# US stock market hours
# The NYSE and the NASDAQ are the two largest American exchanges,
# both of which are located in New York City. Their regular stock
# trading hours are Monday to Friday 9:30 am to 4:30 pm EST (2:30pm to 9pm GMT).
# 2:30pm to 9pm GMT -> 14:30 to 21:00
def get_price(tickers, symbol):
    # if market is open then use "regularMarketPrice"
    # else use "preMarketPrice"

    # utc now
    now = datetime.datetime.utcnow()
    # 14:30
    open_time = datetime.datetime(now.year, now.month, now.day, 14, 30)
    # 21:00
    close_time = datetime.datetime(now.year, now.month, now.day, 21, 0)

    # post market?
    if now > open_time and now < close_time:
        return tickers.tickers[symbol].info["regularMarketPrice"]
    else:
        return tickers.tickers[symbol].info["preMarketPrice"]


def get_yfinance_prices(symbols):
    try:
        tickers = yf.Tickers(" ".join(symbols), timeout=30)
        results = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(symbols)) as executor:
            future_to_symbol = {executor.submit(get_price, tickers, symbol): symbol for (symbol) in symbols}
            for future in concurrent.futures.as_completed(future_to_symbol):
                symbol = future_to_symbol[future]
                try:
                    results[symbol] = future.result()
                except Exception as exc:
                    print(f"{symbol} generated an exception: {exc}")

        return results
    except:
        return dict.fromkeys(symbols)
