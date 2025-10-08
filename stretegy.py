import random

class Strategy:
    def check_signal(self, symbol):
        # Simple random strategy placeholder (replace with real logic)
        signal = random.choice(["BUY", "SELL", None])
        print(f"🧠 {symbol} => Signal: {signal}")
        return signal
