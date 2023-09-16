from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db

from utils.db_api. schemas. user import User
from utils.db_api. schemas. announcement import Fill_Ad_Event
from sqlalchemy import Column, BigInteger, String, sql, BLOB



async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status)
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
async def add_Fill_Ad_Event(photo, date_event: str, time_event: str, description_event: str):
    try:
        fill_Ad_Event = Fill_Ad_Event(photo=photo, date_event=date_event, time_event=time_event, description_event=description_event, )
        await fill_Ad_Event.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')
#_______________________________________________________________________________

