from aiogram import Dispatcher

from .start import router as cmd_start_router
from .callback import router as callback_router

def register_handlers(dp: Dispatcher):
    dp.include_router(cmd_start_router)
    dp.include_router(callback_router)