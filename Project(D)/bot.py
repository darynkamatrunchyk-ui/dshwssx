# bot.py
import telebot
from telebot import custom_filters
from config import BOT_TOKEN
import database

# ІМПОРТУЄМО ФУНКЦІЇ РЕЄСТРАЦІЇ З ПАПКИ HANDLERS
from handlers.start_bot import register_start_handlers
from handlers.horoscope import register_horoscope_handlers
from handlers.callbacks import register_callback_handlers

# Створюємо бота
bot = telebot.TeleBot(BOT_TOKEN, state_storage=telebot.storage.StateMemoryStorage())

# Створюємо базу даних при запуску
database.create_tables()

# Реєструємо всі хендлери
register_start_handlers(bot)
register_horoscope_handlers(bot)
register_callback_handlers(bot)

# Додаємо підтримку станів (States)
bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("✅ Бот запущено! Йди в Телеграм.")
    bot.infinity_polling()