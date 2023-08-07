from aiogram import types
from loader import dp

from utils.db_api import quick_commands as commands


@dp.message_handler(text='/register')
async def command_register(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'ты уже зареган')
        elif user.status == 'bamed':
            await message.answer('Ты забанен')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer('Ты успешно зарегестрирован')

@dp.message_handler(text='/ban')
async def get_ban(message: types.Message):
    await commands.update_status('ban')
    await message.answer('We baned you')

@dp.message_handler(text='/unban')
async def get_unban(message: types.Message):
    await commands.update_status('active')
    await message.answer('We unbaned you')

@dp.message_handler(text='/profile')
async def get_unban(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'Id - {user.first_name}'
                         f'first_name - {user.first_name}'
                         f'last_name - {user.last_name}'
                         f'username - {user.username}'
                         f'status - {user.status}')