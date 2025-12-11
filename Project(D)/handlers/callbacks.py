# handlers/callbacks.py
from telebot import TeleBot
import random

HORO_TEXTS = {
    "today": ["Сьогодні твій день!", "Будь уважним.", "Зірки обіцяють успіх."],
    "tomorrow": ["Завтра відпочинь.", "Готуйся до новин.", "Уникай сварок."],
    "week": ["Тиждень змін.", "Фінансовий ріст.", "Нові знайомства."]
}

def register_callback_handlers(bot: TeleBot):
    @bot.callback_query_handler(func=lambda c: c.data.startswith("horo_"))
    def send_horo(call):
        try:
            _, period, zod = call.data.split("_")
            text = random.choice(HORO_TEXTS.get(period, ["Зірки мовчать..."]))

            bot.edit_message_text(
                f"🔮 Гороскоп для *{zod}*\n\n_{text}_",
                call.message.chat.id,
                call.message.message_id,
                parse_mode="Markdown",
                reply_markup=call.message.reply_markup
            )
        except Exception as e:
            print(f"Error: {e}")