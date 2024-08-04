import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
import random

load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()

recipes = [
    "Салат Цезарь: Романо, куриное филе, пармезан, соус Цезарь.",
    "Паста Карбонара: Спагетти, бекон, яйца, пармезан, черный перец.",
    "Борщ: Свекла, капуста, картофель, морковь, лук, говядина.",
    "Пицца Маргарита: Тесто, томатный соус, моцарелла, базилик.",
    "Омлет с грибами: Яйца, грибы, молоко, сыр, зелень."
]


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(f"Привет,  {message.from_user.first_name}, Добро пожаловать в наш бот.")


@dp.message(Command("myinfo"))
async def user_info(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id} "
                         f"Ваше имя: {message.from_user.first_name}, "
                         f"Ваш никнейм: {message.from_user.username}")


@dp.message(Command("random_recipe"))
async def random_recipe(message: types.Message):
    recipe = random.choice(recipes)
    await message.answer(f"Попробуйте приготовить: {recipe}")


async def start():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
