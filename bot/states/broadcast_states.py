# bot/states/broadcast_states.py
from aiogram.fsm.state import StatesGroup, State

class BroadcastStates(StatesGroup):
    waiting_for_broadcast = State()
