import argparse 
import logging 

from bot.strategy import simple_strategy
from bot.client import BinanceClient 
from bot.orders import create_order 
from bot.validators import validate_order 
from bot.logging_config import setup_logger 

def main():
    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # Normalize input
    args.side = args.side.upper()
    args.type = args.type.upper()

    logging.info(f"CLI Input: {vars(args)}")

    try:
        validate_order(args.symbol, args.side, args.type, args.qty, args.price)

        print("\n📤 ORDER REQUEST")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.qty}")

        if args.type == "LIMIT":
            print(f"Price: {args.price}")

        client = BinanceClient()

        # 🔥 OPTIONAL STRATEGY (SAFE ADD)
        try:
            from bot.strategy import simple_strategy
            decision = simple_strategy(client)

            if decision == "HOLD":
                print("\n🤖 Strategy says HOLD → No trade executed")
                return

            print(f"\n🤖 Strategy Decision: {decision}")
            args.side = decision

        except:
            # If strategy file not present, ignore
            pass

        response = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price
        )

        print("\n✅ ORDER RESULT")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
if __name__ == "__main__": 
    main()