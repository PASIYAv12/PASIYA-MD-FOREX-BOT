from mt5_connector import MT5Connector
from telegram_bot import TelegramBot
from strategy import Strategy
from db import DB
import json, time, threading

def main():
    # Load config
    with open("config.json", "r") as f:
        config = json.load(f)

    mt5 = MT5Connector(config)
    db = DB("bot_data.sqlite")
    strategy = Strategy()
    telegram = TelegramBot(config["TELEGRAM_TOKEN"], db)

    print("🤖 PASIYA-MD FOREX BOT BASE Bot Started")

    def trading_loop():
        while True:
            for pair in config["SYMBOLS"]:
                signal = strategy.check_signal(pair)
                if signal:
                    result = mt5.execute_trade(pair, signal, config["RISK_PER_TRADE"])
                    db.log_trade(pair, signal, result)
                    telegram.notify_trade(pair, signal, result)
            time.sleep(config["CHECK_INTERVAL"])

    threading.Thread(target=trading_loop).start()
    telegram.run()

if __name__ == "__main__":
    main()
