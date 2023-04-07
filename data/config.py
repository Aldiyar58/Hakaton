import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    2141191476,
]


ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATEBESE = str(os.getenv('DATEBESE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATEBESE}'