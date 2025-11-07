from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder

cmd_start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='all position', callback_data='all_position')], [InlineKeyboardButton(text='1 position', callback_data='1_position')],
    [InlineKeyboardButton(text='2 position', callback_data='2_position')], [InlineKeyboardButton(text='3 position', callback_data='3_position')],
    [InlineKeyboardButton(text='4 position', callback_data='4_position')], [InlineKeyboardButton(text='5 position', callback_data='5_position')]
])