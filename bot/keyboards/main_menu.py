# bot/keyboards/main_menu.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def build_main_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Информация о канале", callback_data="info")],
        [InlineKeyboardButton(text="Новости/Обновления", callback_data="news")],
        [InlineKeyboardButton(text="Обратная связь", callback_data="feedback")],
        [InlineKeyboardButton(text="Подписка на приватный канал", callback_data="subscribe")]
    ])
    return keyboard
