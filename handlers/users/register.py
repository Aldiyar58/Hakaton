from aiogram import types
from loader import dp

from utils.db_api import quick_commands as commands
from aiogram.dispatcher import FSMContext

from states import loginInSUH

import requests
from bs4 import BeautifulSoup
import json


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
        await message.answer("Введите свой ИИН или Школную почту")
        await loginInSUH.loginIINorEmail.set()

@dp.message_handler(state=loginInSUH.loginIINorEmail)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(loginIINorEmail=answer)
    await message.answer("Теперь ведите пароль")
    await loginInSUH.next()

@dp.message_handler(state=loginInSUH.password)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(password=answer)
    data = await state.get_data()
    login = data.get('loginIINorEmail')
    password = data.get('password')
    session = requests.Session()
    url_login = "https://sms.ptr.nis.edu.kz/root/Account/LogOn"
    url_user = "https://sms.ptr.nis.edu.kz"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',

    }
    headersForUser = {
        'Content-Type': 'text/html; charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',

    }

    data = {'login': login,
            'password': password,
            'twoFactorAuthCode': "",
            'captchaInput': "",
            'application2FACode': "",
            }

    response_login = session.post(url_login, headers=headers, data=data)
    if json.loads(response_login.text)['success']:
        response_user = session.get(url_user, headers=headers, )
        soup = BeautifulSoup(response_user.text, "lxml")
        body = soup.find("body")
        data_name = body.find_all("script")

        code = str(data_name[1])

        start = code.find('{"UserName":')
        end = code.find('}}});') + 2

        json_str = code[start:end]
        print(json_str)
        data = json.loads(json_str)

        # Извлекаем имя пользователя
        user_name = data['Name']
        print(user_name)

        await message.answer(user_name)

        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                realname=user_name,
                                status='active')
        session.close()
        await state.finish()
    else:
        session.close()
        await message.answer(json.loads(response_login.text)['message'])
        await loginInSUH.loginIINorEmail.set()

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
                         f'realname- {user.realname}'
                         f'status - {user.status}')