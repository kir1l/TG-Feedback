# bot/handlers/news.py
from aiogram import types, Dispatcher
from aiogram.filters import F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_handlers(dp: Dispatcher):
    @dp.callback_query(F.data == "news")
    async def callback_news(callback: types.CallbackQuery):
        news_text = "Новости и обновления: Здесь будут появляться последние новости."
        back_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
        ])
        await callback.message.edit_caption(caption=news_text, reply_markup=back_kb)
        await callback.answer()
