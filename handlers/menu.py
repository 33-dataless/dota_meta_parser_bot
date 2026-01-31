from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def menu(message: Message):
    pass
