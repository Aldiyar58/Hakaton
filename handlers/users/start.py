from aiogram import types
from loader import dp
from utils.db_api import quick_commands as commands

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Чтобы зарегистрироваться пропишите /register')
