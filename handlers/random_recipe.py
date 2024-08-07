from aiogram import Router, types
from aiogram.filters.command import Command
import random

random_router = Router()

recipes = [
    "Салат Цезарь: Романо, куриное филе, пармезан, соус Цезарь.",
    "Паста Карбонара: Спагетти, бекон, яйца, пармезан, черный перец.",
    "Борщ: Свекла, капуста, картофель, морковь, лук, говядина.",
    "Пицца Маргарита: Тесто, томатный соус, моцарелла, базилик.",
    "Омлет с грибами: Яйца, грибы, молоко, сыр, зелень."
]


@random_router.message(Command("random_recipe"))
async def random_recipe(message: types.Message):
    recipe = random.choice(recipes)
    await message.answer(f"Попробуйте приготовить: {recipe}")
