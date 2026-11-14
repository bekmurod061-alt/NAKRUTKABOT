"""Start handler."""
from keyboards import main_menu
from database import save_user

async def start(update, context):
    user = update.effective_user
    save_user(user.id, user.username)
    await update.message.reply_text(
        "Assalomu alaykum! SMM buyurtma botiga xush kelibsiz.",
        reply_markup=main_menu()
    )
