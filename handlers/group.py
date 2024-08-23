from aiogram import Router, F, types
from bot_config import bot
from datetime import timedelta

group_router = Router()
group_router.message.filter(F.chat.type != 'private')

bad_words = ["негодяй", 'болван', "мерзавец", "глупец", "недоумок", "хам", "наглец", "обманщик"]


@group_router.message()
async def filter_bad_words(message: types.Message):
    print(message.text)
    print(message.from_user.first_name)
    txt = message.text
    for i in bad_words:
        if i in txt.lower():
            await message.answer(f"Пользователь {message.from_user.first_name} не надо использовать запретные слова ")
            await message.delete()

            if message.reply_to_message:
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=timedelta(seconds=120)
                )
                await message.delete()
                break
