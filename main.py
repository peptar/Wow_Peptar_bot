from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import os

API_TOKEN = os.getenv('API_TOKEN')  # Токен из переменной окружения

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Клавиатуры
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton(\"Мой персонаж 80-го уровня\"))

goto_ilvl_kb = ReplyKeyboardMarkup(resize_keyboard=True)
goto_ilvl_kb.add(KeyboardButton(\"Окей, какой у тебя ilvl?\"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(\"Привет!\", reply_markup=start_kb)

@dp.message_handler(lambda message: message.text == \"Мой персонаж 80-го уровня\")
async def check_level(message: types.Message):
    await message.answer(\"Окей, какой у тебя ilvl?\", reply_markup=goto_ilvl_kb)

@dp.message_handler(lambda message: message.text == \"Окей, какой у тебя ilvl?\")
async def ask_ilvl(message: types.Message):
    await message.answer(\"Готово\", reply_markup=start_kb)

@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer(\"Пожалуйста, используй кнопки ниже.\", reply_markup=start_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)