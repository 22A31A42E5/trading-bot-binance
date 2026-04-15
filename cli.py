import argparse
import logging
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:
    validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

    client = get_client()
    client.futures_change_leverage(symbol=args.symbol, leverage=1)

    print("\n📊 Order Summary:")
    print(vars(args))

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if "error" in order:
        print("❌ Failed:", order["error"])
        logging.error(order)
    else:
        print("\n✅ Order Placed Successfully")
        print(f"Order ID      : {order.get('orderId')}")
        print(f"Status        : {order.get('status')}")
        print(f"Executed Qty  : {order.get('executedQty')}")
        print(f"Average Price : {order.get('avgPrice')}")

        logging.info(order)

except Exception as e:
    print("❌ Error:", str(e))
    logging.error(str(e))