"""Buyurtma yaratish handlerlari."""
from keyboards import main_menu, service_menu
from database import create_order
from config import ADMIN_ID

SERVICES = {
    "like": "Instagram post layki",
    "view": "Instagram video ko‘rishlari",
    "telegram": "Telegram kanal xizmati"
}

async def handle_callback(update, context):
    q = update.callback_query
    data = q.data
    if data == "order":
        await q.answer()
        await q.edit_message_text("Xizmat turini tanlang:", reply_markup=service_menu())
        return
    if data == "help":
        await q.answer()
        await q.edit_message_text("Yordam uchun administratorga murojaat qiling.", reply_markup=main_menu())
        return
    if data.startswith("service:"):
        await q.answer()
        key = data.split(":", 1)[1]
        context.user_data["service"] = SERVICES.get(key)
        context.user_data["step"] = "link"
        await q.edit_message_text("Havolani yuboring (faqat o‘zingiz boshqaradigan yoki ruxsat olingan sahifa):")
        return
    await q.answer()

async def handle_text(update, context):
    step = context.user_data.get("step")
    if step == "link":
        link = update.message.text.strip()
        if not link.startswith(("https://", "http://")):
            await update.message.reply_text("Havola https:// yoki http:// bilan boshlansin.")
            return
        context.user_data["link"] = link
        context.user_data["step"] = "quantity"
        await update.message.reply_text("Miqdorni kiriting (1–100000):")
    elif step == "quantity":
        try:
            quantity = int(update.message.text.strip())
            if not 1 <= quantity <= 100000:
                raise ValueError
        except ValueError:
            await update.message.reply_text("1 dan 100000 gacha butun son kiriting.")
            return
        user_id = update.effective_user.id
        service = context.user_data["service"]
        link = context.user_data["link"]
        order_id = create_order(user_id, service, link, quantity)
        context.user_data.clear()
        await update.message.reply_text(f"Buyurtma #{order_id} qabul qilindi. Admin tekshiradi.", reply_markup=main_menu())
        if ADMIN_ID:
            await context.bot.send_message(
                ADMIN_ID,
                f"Yangi buyurtma #{order_id}\nFoydalanuvchi: {user_id}\n"
                f"Xizmat: {service}\nHavola: {link}\nMiqdor: {quantity}"
            )
    else:
        await update.message.reply_text("Menyudan bo‘lim tanlang.", reply_markup=main_menu())
