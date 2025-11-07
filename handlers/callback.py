
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.keyboard import cmd_start_keyboard

router = Router()

@router.callback_query(F.data == '1_position')
async def cmd_1_position(callback: CallbackQuery):
    await callback.answer('coming soon')

@router.callback_query(F.data == '2_position')
async def cmd_2_position(callback: CallbackQuery):
    await callback.answer('coming soon')

@router.callback_query(F.data == '3_position')
async def cmd_3_position(callback: CallbackQuery):
    await callback.answer('coming soon')

@router.callback_query(F.data == '4_position')
async def cmd_4_position(callback: CallbackQuery):
    await callback.answer('coming soon')

@router.callback_query(F.data == '5_position')
async def cmd_5_position(callback: CallbackQuery):
    await callback.answer('coming soon')

@router.callback_query(F.data == 'all_position')
async def cmd_all_position(callback: CallbackQuery):
    await callback.answer('coming soon')