from aiogram import Router, types
from aiogram.filters.command import Command

user_info_router = Router()


@user_info_router.message(Command("myinfo"))
async def user_info(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id} "
                         f"Ваше имя: {message.from_user.first_name}, "
                         f"Ваш никнейм: {message.from_user.username}")

