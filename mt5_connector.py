import MetaTrader5 as mt5

class MT5Connector:
    def __init__(self, config):
        self.config = config
        self.connect()

    def connect(self):
        mt5.initialize(login=self.config["ACCOUNT_LOGIN"],
                       password=self.config["ACCOUNT_PASSWORD"],
                       server=self.config["ACCOUNT_SERVER"])
        print("✅ Connected to MT5")

    def execute_trade(self, symbol, signal, risk):
        lot = 0.01 * risk
        price = mt5.symbol_info_tick(symbol).ask if signal == "BUY" else mt5.symbol_info_tick(symbol).bid
        order_type = mt5.ORDER_TYPE_BUY if signal == "BUY" else mt5.ORDER_TYPE_SELL
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": order_type,
            "price": price,
            "deviation": 10,
            "magic": 123456,
            "comment": "PASIYA-MD-FOREX-BOT-BASE",
        }
        result = mt5.order_send(request)
        print(f"📊 {symbol} {signal} -> {result}")
        return result
