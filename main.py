# main.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from bot import config
from bot.router import register_all_handlers
from bot.utils.logger import setup_logging
from bot.db import init_db

async def main():
    # Настраиваем логирование
    setup_logging()
    
    # Инициализируем базу данных (если требуется)
    init_db()
    
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Централизованная регистрация всех обработчиков
    register_all_handlers(dp)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
