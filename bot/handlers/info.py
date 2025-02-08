# bot/handlers/info.py
from aiogram import types, Dispatcher
from aiogram.filters import F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_handlers(dp: Dispatcher):
    @dp.callback_query(F.data == "info")
    async def callback_info(callback: types.CallbackQuery):
        info_text = "Информация о канале: Здесь можно узнать подробности о канале."
        back_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
        ])
        await callback.message.edit_caption(caption=info_text, reply_markup=back_kb)
        await callback.answer()
