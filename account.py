"""Kabinet va buyurtmalar tarixi."""
from database import get_balance, user_orders
from keyboards import back_menu

async def account_callback(update, context):
    q = update.callback_query
    await q.answer()
    if q.data == "account":
        balance = get_balance(q.from_user.id)
        await q.edit_message_text(f"👤 ID: {q.from_user.id}\n💰 Balans: {balance:.2f} so‘m", reply_markup=back_menu())
    elif q.data == "orders":
        rows = user_orders(q.from_user.id)
        message = "Hozircha buyurtmalar yo‘q." if not rows else "\n".join(
            f"#{r[0]} — {r[1]} — {r[2]} dona — {r[3]}" for r in rows
        )
        await q.edit_message_text("📦 Buyurtmalaringiz:\n" + message, reply_markup=back_menu())
    elif q.data == "menu":
        from keyboards import main_menu
        await q.edit_message_text("Asosiy menyu:", reply_markup=main_menu())
