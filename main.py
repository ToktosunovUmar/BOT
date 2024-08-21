import asyncio
import logging

from bot_config import bot, dp, database
from handlers import (
    private_router
)


async def start_up(bot):
    print("запустился")
    database.create_tables()


async def start():
    dp.include_router(private_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
