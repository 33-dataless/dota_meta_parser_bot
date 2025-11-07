from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards.keyboard import cmd_start_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, command: CommandStart):
    await message.answer(f'Привет {message.from_user.first_name}! Что хочешь узнать?', reply_markup=cmd_start_keyboard)

