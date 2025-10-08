from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

class TelegramBot:
    def __init__(self, token, db):
        self.bot = Bot(token)
        self.db = db
        self.app = ApplicationBuilder().token(token).build()

        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("trades", self.show_trades))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🚀 PASIYA-MD FOREX BIT BASE Online!")

    async def show_trades(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        trades = self.db.conn.execute("SELECT * FROM trades ORDER BY id DESC LIMIT 5").fetchall()
        msg = "\n".join([f"{t[1]} {t[2]} {t[3]}" for t in trades]) or "No trades yet."
        await update.message.reply_text(msg)

    async def notify_trade(self, symbol, signal, result):
        await self.bot.send_message(chat_id=self.db.conn, text=f"{symbol} {signal} {result}")

    def run(self):
        asyncio.run(self.app.run_polling())
