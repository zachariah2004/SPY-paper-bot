import os
from alpaca.trading.client import TradingClient

api_key = os.environ["APCA_API_KEY_ID"]
secret_key = os.environ["APCA_API_SECRET_KEY"]

client = TradingClient(
    api_key=api_key,
    secret_key=secret_key,
    paper=True
)

account = client.get_account()

print("PAPER CONNECTION SUCCESS")
print("Account status:", account.status)
print("Buying power:", account.buying_power)