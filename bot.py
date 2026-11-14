"""Telegram SMM order bot entry point."""
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import BOT_TOKEN
from database import init_db
from start import start
from order import handle_callback, handle_text
from account import account_callback
from admin import admin_command, status_command

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN .env faylida sozlanmagan.")
    init_db()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CallbackQueryHandler(account_callback, pattern=r"^(account|orders|menu)$"))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()

if __name__ == "__main__":
    main()
