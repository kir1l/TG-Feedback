# bot/states/admin_states.py
from aiogram.fsm.state import StatesGroup, State

class AdminReplyStates(StatesGroup):
    waiting_for_reply = State()
