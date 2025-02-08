# bot/handlers/feedback.py
from aiogram import types, Dispatcher, Bot
from aiogram.filters import F
from aiogram.fsm.context import FSMContext
from bot.states.feedback_states import FeedbackStates
from bot.keyboards.main_menu import build_main_menu
from bot.config import ADMIN_ID

def register_handlers(dp: Dispatcher):
    @dp.callback_query(F.data == "feedback")
    async def callback_feedback(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_caption(caption="Введите текст обратной связи:", reply_markup=None)
        await state.set_state(FeedbackStates.waiting_for_feedback)
        await callback.answer()

    @dp.message(FeedbackStates.waiting_for_feedback)
    async def process_feedback(message: types.Message, state: FSMContext):
        feedback_text = message.text
        user = message.from_user
        feedback_message = (
            f"<b>Обратная связь от пользователя:</b>\n"
            f"ID: {user.id}\n"
            f"Имя: {user.first_name}\n"
            f"Фамилия: {user.last_name or 'Не указана'}\n"
            f"Username: @{user.username or 'Нет'}\n\n"
            f"<b>Текст:</b> {feedback_text}"
        )
        from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
        reply_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Ответить", callback_data=f"reply_{user.id}")]
        ])
        await message.bot.send_message(ADMIN_ID, feedback_message, reply_markup=reply_kb)
        await message.answer("Спасибо за ваш отзыв!", reply_markup=build_main_menu())
        await state.clear()

    @dp.callback_query(F.data == "back_to_menu")
    async def callback_back_to_menu(callback: types.CallbackQuery):
        from bot.keyboards.main_menu import build_main_menu
        main_text = "Добро пожаловать в наш канал! Выберите нужный раздел:"
        await callback.message.edit_caption(caption=main_text, reply_markup=build_main_menu())
        await callback.answer()
