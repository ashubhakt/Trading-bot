# Trading Bot (Binance Futures Testnet)

##  Overview
A modular Python-based trading bot that allows users to place market and limit orders via CLI.

##  Setup
1. Create project folder
2. Add API keys in `.env`

##  Install
pip install -r requirements.txt

##  Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 30000

##  Features
- CLI-based trading bot
- Market & Limit order support
- Input validation
- Logging system
- Modular architecture

##  Structure
- client.py → API connection  
- orders.py → order execution logic  
- validators.py → input validation  
- cli.py → entry point  

##  Note
This project uses a simulated order execution system instead of real Binance API order placement.

To enable real trading, replace the mock response in `orders.py` with actual Binance API calls.