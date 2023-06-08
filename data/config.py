import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    2141191476,
]


ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATEBESE = str(os.getenv('DATABASE'))


connection = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATEBESE}'
