from aiogram import types
from loader import bot, dp
from loader import dp
import time
from utils.db_api import quick_commands as commands

async def send_announcement_daily():
    for event in await commands.select_all_event():
        print(event.date_event)
        print(time.strftime("%d/%m/%Y"))
        if event.date_event == time.strftime("%d/%m/%Y"):
            print('good')
            for id in event.chat_id_list:
                print(id)
                await bot.send_photo(chat_id=id, photo=event.photo, caption=f'{event.name}\n\n'
                                                                      f'{event.date_event}\n\n'
                                                                      f'{event.time_event}\n\n'
                                                                      f'{event.description_event}\n'
                                                                      f'{event.person}')