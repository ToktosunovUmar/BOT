from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

dialog_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@dialog_router.callback_query(F.data == "feedback")
async def start_feedback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)


@dialog_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш номер телефона:")
    await state.set_state(RestourantReview.phone_number)


@dialog_router.message(RestourantReview.phone_number)
async def process_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Когда вы посетили наш ресторан? (укажите дату)")
    await state.set_state(RestourantReview.visit_date)


@dialog_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    visit_date = message.text
    if not visit_date.isdigit():
        await message.answer("Вводите только цифры")
        return
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="плохо"),
                types.KeyboardButton(text="удовлетворительно")
            ],
            [
                types.KeyboardButton(text="хорошо"),
                types.KeyboardButton(text="великолепно")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Оцените качество еды:", reply_markup=kb)
    await state.update_data(visit_date=message.text)
    await state.set_state(RestourantReview.food_rating)


@dialog_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await message.answer("Оцените чистоту:")
    await state.set_state(RestourantReview.cleanliness_rating)


@dialog_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("Оставьте любые дополнительные комментарии:")
    await state.set_state(RestourantReview.extra_comments)


@dialog_router.message(RestourantReview.extra_comments)
async def process_extra_comments(state: FSMContext):
    await state.clear()
