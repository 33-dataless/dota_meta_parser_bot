from aiogram import Dispatcher

from middlewares.middleware import DataBaseMiddleWare

from .start import router as cmd_start_router
from .callback import router as callback_router


def register_handlers(dp: Dispatcher):
    dp.update.outer_middleware(DataBaseMiddleWare())
    dp.include_router(cmd_start_router)
    dp.include_router(callback_router)