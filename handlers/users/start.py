from aiogram import types
from loader import dp
from utils.db_api import quick_commands as commands

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Чтобы зарегистрироваться пропишите /register')
    print(await commands.select_all_event())
    print(type(await commands.select_all_event()))
    print()
    user = await commands.select_user(message.from_user.id)
    print(user)
    print(type(user))

    events = await commands.select_all_event()
    for i in events:
        print(i.name)
        print(type(i))