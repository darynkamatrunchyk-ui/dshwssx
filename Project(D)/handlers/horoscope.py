from telebot import TeleBot
from states.user_states import UserState
import database
from keyboards import reply, inline


def register_horoscope_handlers(bot: TeleBot):
    # 1. Виправлено текст: "Скасувати" (без пробілу)
    @bot.message_handler(state="*", func=lambda m: m.text == "Скасувати")
    def cancel_action(msg):
        bot.send_message(msg.chat.id, "Дію скасовано.", reply_markup=reply.main_menu())
        bot.delete_state(msg.from_user.id, msg.chat.id)

    # 2. Виправлено текст: "Обрати знак" (без пробілу)
    @bot.message_handler(func=lambda m: m.text == "Обрати знак")
    def choose_zodiac(msg):
        bot.set_state(msg.from_user.id, UserState.choosing_zodiac, msg.chat.id)
        bot.send_message(msg.chat.id, "Обери свій знак зодіаку:", reply_markup=reply.cancel_menu())
        bot.send_message(msg.chat.id, "Список:", reply_markup=inline.zodiac_menu())

    # Хендлер для інлайн-кнопок (тут все ок)
    @bot.callback_query_handler(func=lambda c: c.data.startswith("zodiac_"))
    def zodiac_selected(call):
        zod = call.data.split("_")[1]
        database.set_user_zodiac(call.from_user.id, zod)

        bot.delete_state(call.from_user.id, call.message.chat.id)
        bot.answer_callback_query(call.id)

        bot.send_message(call.message.chat.id, "Знак збережено!", reply_markup=reply.main_menu())
        bot.send_message(call.message.chat.id, f"Твій знак: {zod}", reply_markup=inline.horoscope_period_menu(zod))

    # 3. Виправлено текст: "Мій гороскоп" (без пробілу)
    @bot.message_handler(func=lambda m: m.text == "Мій гороскоп")
    def my_horo(msg):
        z = database.get_user_zodiac(msg.from_user.id)
        if not z:
            bot.send_message(msg.chat.id, "Спершу обери знак!", reply_markup=reply.main_menu())
            return

        bot.send_message(msg.chat.id, f"Обери період для {z}:", reply_markup=inline.horoscope_period_menu(z))