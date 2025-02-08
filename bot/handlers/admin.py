# bot/handlers/admin.py
from aiogram import types, Dispatcher
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot.states.admin_states import AdminReplyStates
from bot.states.broadcast_states import BroadcastStates
from bot.config import ADMIN_IDS
from bot.db import get_subscribers

def register_handlers(dp: Dispatcher):
    @dp.callback_query(F.data.startswith("reply_"))
    async def admin_reply_callback(callback: types.CallbackQuery, state: FSMContext):
        # Проверяем, что пользователь является администратором
        if callback.from_user.id not in ADMIN_IDS:
            await callback.answer("У вас нет прав для этого действия.", show_alert=True)
            return
        target_user_id = int(callback.data.split("_")[1])
        await state.update_data(target_user_id=target_user_id)
        await callback.message.answer("Введите ответ для пользователя:")
        await state.set_state(AdminReplyStates.waiting_for_reply)
        await callback.answer()

    @dp.message(AdminReplyStates.waiting_for_reply)
    async def process_admin_reply(message: types.Message, state: FSMContext):
        data = await state.get_data()
        target_user_id = data.get("target_user_id")
        reply_text = message.text
        try:
            await message.bot.send_message(target_user_id, f"<b>Ответ от администрации:</b>\n\n{reply_text}")
            await message.answer("Ваш ответ отправлен пользователю.")
        except Exception:
            await message.answer("Не удалось отправить ответ пользователю.")
        await state.clear()

    @dp.message(Command("broadcast"))
    async def cmd_broadcast(message: types.Message, state: FSMContext):
        # Проверка, что отправитель команды входит в список администраторов
        if message.from_user.id not in ADMIN_IDS:
            return
        await message.answer("Введите сообщение для рассылки:")
        await state.set_state(BroadcastStates.waiting_for_broadcast)

    @dp.message(BroadcastStates.waiting_for_broadcast)
    async def process_broadcast(message: types.Message, state: FSMContext):
        broadcast_text = message.text
        subscribers = get_subscribers()
        count = 0
        for user_id in subscribers:
            try:
                await message.bot.send_message(user_id, broadcast_text)
                count += 1
            except Exception:
                continue
        await message.answer(f"Рассылка завершена. Сообщение отправлено {count} пользователям.")
        await state.clear()
