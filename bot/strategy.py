from binance.client import Client

def simple_strategy(client):
    price_data = client.client.futures_symbol_ticker(symbol="BTCUSDT")
    price = float(price_data["price"])

    print(f"Current BTC Price: {price}")

    # SIMPLE LOGIC
    if price < 50000:
        return "BUY"
    elif price > 80000:
        return "SELL"
    else:
        return "HOLD"