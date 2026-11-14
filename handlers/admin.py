
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from config import ADMIN ID
from database import stats, update_order_status


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN ID:
        await update.message.reply_text("⛔ Sizda admin huquqi yo‘q!")
        return

    users, orders, pending = stats()

    text = (
        "🛠 ADMIN PANEL\n\n"
        f"👥 Foydalanuvchilar: {users}\n"
        f"📦 Jami buyurtmalar: {orders}\n"
        f"🆕 Yangi buyurtmalar: {pending}\n\n"
        "Buyurtma holati:\n"
        "/status ID Bajarildi"
    )

    await update.message.reply_text(text)


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN ID:
        await update.message.reply_text("⛔ Ruxsat yo‘q!")
        return

    if len(context.args) < 2:
        await update.message.reply_text(
            "Format: /status ID Bajarildi"
        )
        return

    try:
        order_id = int(context.args[0])
        status = " ".join(context.args[1:])
        count, user_id = update_order_status(order_id, status)

        if not count:
            await update.message.reply_text("❌ Buyurtma topilmadi!")
            return

        await update.message.reply_text(
            f"✅ #{order_id} buyurtma holati: {status}"
        )

        if user_id:
            await context.bot.send_message(
                user_id,
                f"📢 Buyurtmangiz holati: {status}"
            )

    except ValueError:
        await update.message.reply_text("8982978887")


admin_handler = CommandHandler("admin", admin_panel)
status_handler = CommandHandler("status", status_command)

