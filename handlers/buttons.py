from aiogram import types, Router, F
from aiogram.filters.command import Command
from bot_config import database
from aiogram.types import FSInputFile

buttons_router = Router()


@buttons_router.message(Command("menu"))
async def menu(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="drinks", callback_data='drinks'),
            ],
            [
                types.InlineKeyboardButton(text='roast', callback_data='roast')
            ],
            [
                types.InlineKeyboardButton(text="soup", callback_data="soup")
            ]
        ]
    )
    await message.answer('Выберите категорию блюд', reply_markup=kb)


signal = ('dinks', 'roast', "soup")


@buttons_router.callback_query(lambda call: call.data in signal)
async def dishes(call: types.CallbackQuery):
    query = """
    SELECT * FROM dishes JOIN categories ON dishes.category_id = categories.id WHERE categories.name = ?
    """

    data = database.fetch(
        query=query,
        params=(call.data,)
    )
    for i in data:
        photo = FSInputFile(i[3])
        await call.message.answer_photo(photo=photo, caption=f'name: {i[1]}\n'
                                                             f'price: {i[2]}\n')

