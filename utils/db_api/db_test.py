import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config.connection)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'Vlad', 'net')
    await commands.add_user(789456, 'dddd', 'hfhfhj')
    await commands.add_user(123456, 'bot', 'ssgs')
    await commands.add_user(8, 'telegram', 'sdlkhgs')
    await commands.add_user(7897897, 'Vlad', '4545')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, 'new vlaD NAME')

    user = await commands.select_user(1)
    print(user)

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
