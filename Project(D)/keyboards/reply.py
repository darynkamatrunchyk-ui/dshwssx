from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    # Зверни увагу: текст без пробілів на початку!
    kb.add(KeyboardButton("Мій гороскоп"))
    kb.add(KeyboardButton("Обрати знак"))
    return kb

def cancel_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Скасувати"))
    return kb