# bot/handlers/start.py
from aiogram import types, Dispatcher
from aiogram.filters import Command
from bot.keyboards.main_menu import build_main_menu
from bot.db import add_subscriber
from bot.config import ADMIN_ID  # если нужно использовать

def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        add_subscriber(message.from_user.id)
        text = "Добро пожаловать в наш канал! Выберите нужный раздел:"
        # Укажите актуальный URL фотографии
        photo_url = "https://example.com/photo.jpg"
        await message.answer_photo(photo=photo_url, caption=text, reply_markup=build_main_menu())
