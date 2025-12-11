# states/user_states.py
from telebot.handler_backends import State, StatesGroup

class UserState(StatesGroup):
    choosing_zodiac = State()