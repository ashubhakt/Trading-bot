# Trading Bot (Binance Futures Testnet)

## Setup
1. Create project folder
2. Add API keys in `.env`

## Install
pip install python-binance python-dotenv

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 30000

## Features
- CLI-based trading bot
- Market & Limit order support
- Input validation
- Logging system
- Modular architecture

## Structure
- client.py → API connection
- orders.py → order execution logic
- validators.py → input validation
- cli.py → entry point

## Note

This project uses a simulated order execution system instead of real Binance API order placement.

Due to regional/API access limitations, actual API keys could not be generated.  
However, the system is fully designed to support real API integration — only the execution layer needs to be switched.

All components such as validation, logging, and order structure are implemented as per real-world trading systems.

To enable real trading, replace the mock response in `orders.py` with actual Binance API call.