from aiogram import types
from loader import dp
from loader import bot

ch_id = '-1001775529848'
@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    text = "new_news"
    await bot.send_message(message.from_user.id, message.chat.id)



