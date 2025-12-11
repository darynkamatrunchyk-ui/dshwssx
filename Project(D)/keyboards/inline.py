# keyboards/inline.py
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config

def zodiac_menu():
    kb = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for z in config.ZODIAC_SIGNS:
        buttons.append(InlineKeyboardButton(text=z, callback_data=f"zodiac_{z}"))
    kb.add(*buttons)
    return kb

def horoscope_period_menu(zod):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Сьогодні", callback_data=f"horo_today_{zod}"),
        InlineKeyboardButton("Завтра", callback_data=f"horo_tomorrow_{zod}")
    )
    kb.add(InlineKeyboardButton("Тиждень", callback_data=f"horo_week_{zod}"))
    return kb