import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
import logging


from handlers.random_recipe import random_router
from handlers.user_info import user_info_router
from handlers.send_welcome import send_welcome_router
from handlers.dishes import dishes_router


load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()


async def start():
    dp.include_router(send_welcome_router)
    dp.include_router(user_info_router)
    dp.include_router(random_router)
    dp.include_router(dishes_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
