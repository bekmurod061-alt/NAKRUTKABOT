"""Telegram inline klaviaturalari."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Buyurtma berish", callback_data="order")],
        [InlineKeyboardButton("👤 Kabinetim", callback_data="account")],
        [InlineKeyboardButton("📦 Buyurtmalarim", callback_data="orders")],
        [InlineKeyboardButton("ℹ️ Yordam", callback_data="help")]
    ])

def service_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Instagram post layki", callback_data="service:like")],
        [InlineKeyboardButton("Instagram video ko‘rishlari", callback_data="service:view")],
        [InlineKeyboardButton("Telegram kanal xizmati", callback_data="service:telegram")],
        [InlineKeyboardButton("⬅️ Menyu", callback_data="menu")]
    ])

def back_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Menyu", callback_data="menu")]])
