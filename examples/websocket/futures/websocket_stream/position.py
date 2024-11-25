import logging

from bitmart.lib.cloud_consts import FUTURES_PRIVATE_WS_URL
from bitmart.lib.cloud_utils import config_logging
from bitmart.websocket.futures_socket_client import FuturesSocketClient

config_logging(logging, logging.INFO)


def message_handler(message):
    logging.info(f"message_handler: {message}")


my_client = FuturesSocketClient(stream_url=FUTURES_PRIVATE_WS_URL,
                                on_message=message_handler,
                                api_key="your_api_key",
                                api_secret_key="your_secret_key",
                                api_memo="your_api_memo")

# Login
my_client.login(timeout=5)

# Subscribe to a single symbol stream
my_client.subscribe(args="futures/position")


# Stop
# my_client.stop()
