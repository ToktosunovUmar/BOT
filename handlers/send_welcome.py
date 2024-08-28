from aiogram import Router, types, F
from aiogram.filters.command import Command

send_welcome_router = Router()


@send_welcome_router.message(Command("start"))
async def send_welcome(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="наш адрес", callback_data='adress'),
                types.InlineKeyboardButton(text='instagram', url='https://www.instagram.com/barashek.restaurant/')
            ],
            [
                types.InlineKeyboardButton(text="наш сайт", url='https://barashek.kg/')
            ],
            [
                types.InlineKeyboardButton(text="оставить отзыв", callback_data="feedback")
            ],
            [
                types.InlineKeyboardButton(text="дома", callback_data="house")
            ]
        ]

    )
    await message.answer(f"Привет,  {message.from_user.first_name}, Добро пожаловать в наш бот.", reply_markup=kb)


@send_welcome_router.callback_query(F.data == 'adress')
async def about_us_handler(callback):
    await callback.message.answer('Наш адрес: ул. Примерная, 123')

