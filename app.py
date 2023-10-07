async def on_startup(dp):

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('Подключение к Postgre')
    await on_startup(dp)

    # print('Удаление базы данных')
    # await db.gino.drop_all()

    print('Создание таблиц')
    await db.gino.create_all()
    print("Готова")


    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('bot start')
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    from utils.SendDailyAno import send_announcement_daily
    from datetime import datetime, timedelta
    from loader import bot
    scheduler = AsyncIOScheduler(timezone="Asia/Almaty")
    scheduler.add_job(send_announcement_daily, trigger='cron', hour=datetime.now().hour,
                      minute=datetime.now().minute + 1, start_date=datetime.now())
    scheduler.start()
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
