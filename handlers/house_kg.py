from aiogram import Router, types, F
from crawel.house_rental import house_crawler

house_router = Router()


@house_router.callback_query(F.data == "house")
async def show_house(callback: types.CallbackQuery):
    crawler = house_crawler()
    crawler.get_page()
    links = crawler.get_house_links()
    for link in links:
        await callback.message.answer(link)
