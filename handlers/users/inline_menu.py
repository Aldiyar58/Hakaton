from aiogram import types

from keyboard.inline import ikb_info_type
from loader import dp

@dp.message_handler(text="Инлайн меню")
async def show_inline_menu(message: types.Message):
    await message.answer('Инлайн кнопки ниже', reply_markup=ikb_info_type)
