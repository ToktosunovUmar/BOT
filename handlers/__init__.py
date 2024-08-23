from aiogram import F, Router


from .send_welcome import send_welcome_router
from .dishes import dishes_router
from .review_dialog import dialog_router
from .random_recipe import random_router
from .user_info import user_info_router
from .buttons import buttons_router
from .group import group_router

private_router = Router()

private_router.include_router(send_welcome_router)
private_router.include_router(user_info_router)
private_router.include_router(random_router)
private_router.include_router(dishes_router)
private_router.include_router(dialog_router)
private_router.include_router(buttons_router)



private_router.message.filter(F.chat.type == "private")
