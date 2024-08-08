import asyncio
import logging


from bot_config import bot, dp
from handlers.random_recipe import random_router
from handlers.user_info import user_info_router
from handlers.send_welcome import send_welcome_router
from handlers.dishes import dishes_router


async def start():
    dp.include_router(send_welcome_router)
    dp.include_router(user_info_router)
    dp.include_router(random_router)
    dp.include_router(dishes_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
