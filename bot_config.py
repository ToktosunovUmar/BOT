from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from database.database import DataBase

load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
database = DataBase("db.sqlite3")
