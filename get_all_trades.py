import logging
from binance.um_futures import UMFutures
from binance.error import ClientError
from get_keys import get_api_key

api_key, secret = get_api_key()
um_futures_client = UMFutures(key=api_key, secret=secret)


def get_trades():
    # Get Binance api keys
    symbols = ["XRPUSDT", "BTCUSDT", "ADAUSDT", "BLZUSDT", "1000PEPEUSDT", "BAKEUSDT", "ETHUSDT"]
    all_trades = []
    # Fetch trades for each symbol and append them to the all_trades list
    for symbol in symbols:
        trades = um_futures_client.get_account_trades(symbol=symbol, recvWindow=6000)
        all_trades.extend(trades)
    print(f"These coins are included: {symbols} \n If you want other coins to be included add them to symbols list in get_trades()" )
    return all_trades

get_trades()
