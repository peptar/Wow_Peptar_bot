from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import os

# Получаем токен из переменной окружения
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Клавиатура: стартовая
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("Мой персонаж 80-го уровня"))

# Клавиатура: вопрос про ilvl
goto_ilvl_kb = ReplyKeyboardMarkup(resize_keyboard=True)
goto_ilvl_kb.add(KeyboardButton("Окей, какой у тебя ilvl?"))

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!", reply_markup=start_kb)

# Пользователь говорит, что у него персонаж 80-го уровня
@dp.message_handler(lambda message: message.text == "Мой персонаж 80-го уровня")
async def check_level(message: types.Message):
    await message.answer("Окей, какой у тебя ilvl?", reply_markup=goto_ilvl_kb)

# Пользователь отвечает про ilvl
@dp.message_handler(lambda message: message.text == "Окей, какой у тебя ilvl?")
async def ask_ilvl(message: types.Message):
    await message.answer("Готово", reply_markup=start_kb)

# Обработка всего остального
@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer("Пожалуйста, используй кнопки ниже.", reply_markup=start_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
