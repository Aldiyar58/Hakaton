from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db

from utils.db_api. schemas. user import User
from utils.db_api. schemas. announcement import Fill_Ad_Event
from sqlalchemy import Column, BigInteger, String, sql, BLOB



async def add_user(user_id: int, first_name: str, last_name: str, username: str, realname: str, status: str):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, realname=realname, status=status)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
     users = await User.query.gino.all()
     return users

async def count_users():
    count = db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
     user = await User.query.where(User.user_id == user_id).gino.first()
     return user

async def update_status(user_id, status):
     user = await select_user(user_id)
     await user.update(status=status).apply()






async def add_Fill_Ad_Event(photo, date_event: str,name: str, time_event: str, description_event: str, person: str, chat_id_list: list):
    try:
        fill_Ad_Event = Fill_Ad_Event(photo=photo, name=name, date_event=date_event, time_event=time_event, description_event=description_event, person=person, chat_id_list=chat_id_list )
        await fill_Ad_Event.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_event():
    events = await Fill_Ad_Event.query.gino.all()
    return events

async def select_event_by_date(date_event):
    events = Fill_Ad_Event.query.where(Fill_Ad_Event.date_event == date_event).gino
    return events

#_______________________________________________________________________________

