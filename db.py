import sqlite3

class DB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            signal TEXT,
            result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")

    def log_trade(self, symbol, signal, result):
        self.conn.execute("INSERT INTO trades(symbol, signal, result) VALUES (?, ?, ?)",
                          (symbol, signal, str(result)))
        self.conn.commit()
