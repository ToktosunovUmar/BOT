from aiogram import Router, F, types
from bot_config import bot
from datetime import timedelta

group_router = Router()
group_router.message.filter(F.chat.type != 'private')

bad_words = ["негодяй", "сука", 'болван', "мерзавец", "глупец", "недоумок", "хам", "наглец", "обманщик"]


@group_router.message()
async def filter_bad_words(message: types.Message):
    txt = message.text
    for word in bad_words:
        if word in txt.lower():
            await message.answer(f"Пользователь {message.from_user.first_name} "
                                 f"не надо использовать запретные слова ")
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id,
                until_date=timedelta(seconds=30)
            )
            await message.delete()
            break
