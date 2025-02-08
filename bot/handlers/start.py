# bot/handlers/start.py
from aiogram import types, Dispatcher
from aiogram.filters import Command
from bot.keyboards.main_menu import build_main_menu
from bot.db import add_subscriber
from bot.config import ADMIN_IDS  # если нужно использовать
from pathlib import Path
from aiogram.types import FSInputFile

def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        add_subscriber(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        text = "Добро пожаловать в наш канал! Выберите нужный раздел:"
        photo_path = Path(__file__).parent.parent / "assets" / "main_bg.JPG"
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo=photo, caption=text, reply_markup=build_main_menu())
