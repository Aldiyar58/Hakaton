from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboard.default import kb_menu
from keyboard.inline import ikb_info_type
from loader import dp

@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
    await message.answer("Текст", reply_markup=ikb_info_type)

