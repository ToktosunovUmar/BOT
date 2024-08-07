from aiogram import Router, types, F

dishes_router = Router()


@dishes_router.message(F.text.lower() == "холодные напитки")
async def cold_drink(message: types.Message):
    image = types.FSInputFile("images/cold_drink.jpg")
    await message.answer_photo(image, caption="Лимонад")


@dishes_router.message(F.text.lower() == "манты")
async def cold_drink(message: types.Message):
    image = types.FSInputFile("images/manty.jpg")
    await message.answer_photo(image, caption="Манты")
