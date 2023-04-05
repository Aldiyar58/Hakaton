from aiogram import Bot, Dispatcher, types

from data import config

# Создоём переменную бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# create Dispatcher
dp = Dispatcher(bot)
