# handlers/start_bot.py
from telebot import TeleBot
from keyboards import reply

def register_start_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def start_cmd(msg):
        bot.send_message(
            msg.chat.id,
            f"Привіт, {msg.from_user.first_name}! \n"
            f"Я — бот гороскопів. Обери дію в меню 👇",
            reply_markup=reply.main_menu()
        )