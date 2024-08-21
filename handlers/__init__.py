from aiogram import F, Router
from bot_config import dp

from .send_welcome import send_welcome_router
from .dishes import dishes_router
from .review_dialog import dialog_router
from .random_recipe import random_router
from .user_info import user_info_router
from .buttons import buttons_router


private_router = Router()

dp.include_router(send_welcome_router)
dp.include_router(user_info_router)
dp.include_router(random_router)
dp.include_router(dishes_router)
dp.include_router(dialog_router)
dp.include_router(buttons_router)

private_router.message.filter(F.chat.type == "private")