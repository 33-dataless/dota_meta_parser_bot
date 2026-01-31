from aiogram import Dispatcher

from middlewares.middleware import DataBaseMiddleWare

from .callback import router as callback_router
from .menu import router as menu_router

def register_handlers(dp: Dispatcher):
    dp.update.outer_middleware(DataBaseMiddleWare())
    dp.include_router(callback_router)
    dp.include_router(menu_router)