
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from database import (
    save_user,
    get_balance,
    user_orders
)


async def user_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    save_user(user.id, user.username)

    await update.message.reply_text(
        "👋 Assalomu alaykum!\n\n"
        "🤖 SMM xizmatlar botiga xush kelibsiz!\n\n"
        "Kerakli bo‘limni menyudan tanlang."
    )


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    balance = get_balance(user.id)

    text = (
        "👤 MENING KABINETIM\n\n"
        f"🆔 ID: {user.id}\n"
        f"👨‍💻 Username: @{user.username or 'mavjud emas'}\n"
        f"💰 Balans: {balance:.2f} so‘m"
    )

    await update.message.reply_text(text)


async def my_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    orders = user_orders(user.id)

    if not orders:
        await update.message.reply_text(
            "📦 Sizda hali buyurtmalar mavjud emas."
        )
        return

    text = "📦 BUYURTMALAR TARIXI\n\n"

    for order in orders:
        text += (
            f"🆔 Buyurtma: #{order[0]}\n"
            f"🛒 Xizmat: {order[1]}\n"
            f"🔢 Miqdor: {order[2]}\n"
            f"📌 Holat: {order[3]}\n\n"
        )

    await update.message.reply_text(text)


profile_handler = CommandHandler("profile", profile)
orders_handler = CommandHandler("orders", my_orders)
