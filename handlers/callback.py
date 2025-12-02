
from aiogram import Router, F
from aiogram.types import CallbackQuery
from main_parser.mainparser import DotaParser
from keyboards.keyboard import cmd_start_keyboard

router = Router()

def refact_answer(answer: list, mess: str):
    return f"""
⏱️ данные обновлены: {answer[0][-1]}

{mess} 

1   {answer[0][0]} | d2pt {answer[0][1]} | {answer[0][2]} | {answer[0][-2]}%
2   {answer[1][0]} | d2pt {answer[1][1]} | {answer[1][2]} | {answer[1][-2]}%
3   {answer[2][0]} | d2pt {answer[2][1]} | {answer[2][2]} | {answer[2][-2]}%
4   {answer[3][0]} | d2pt {answer[3][1]} | {answer[3][2]} | {answer[3][-2]}%
5   {answer[4][0]} | d2pt {answer[4][1]} | {answer[4][2]} | {answer[4][-2]}%
6   {answer[5][0]} | d2pt {answer[5][1]} | {answer[5][2]} | {answer[5][-2]}%
7   {answer[6][0]} | d2pt {answer[6][1]} | {answer[6][2]} | {answer[6][-2]}%
8   {answer[7][0]} | d2pt {answer[7][1]} | {answer[7][2]} | {answer[7][-2]}%
9   {answer[8][0]} | d2pt {answer[8][1]} | {answer[8][2]} | {answer[8][-2]}%
10  {answer[9][0]} | d2pt {answer[9][1]} | {answer[9][2]} | {answer[9][-2]}%"""

def get_answer(link: str, mess: str):
    dotaparser = DotaParser()
    response = dotaparser.get_response(link=link)
    vector = dotaparser.create_vector(response=response)
    return refact_answer(vector, mess=mess)
    
@router.callback_query(F.data == 'all_position')
async def cmd_all_position(callback: CallbackQuery):
    mess = "🩸 Все позиции"
    answer = get_answer(link=DotaParser.link_all_position, mess=mess)
    await callback.message.edit_text(answer, reply_markup=cmd_start_keyboard)

@router.callback_query(F.data == '1_position')
async def cmd_1_position(callback: CallbackQuery):
    mess = "🗡 Керри"
    answer = get_answer(link=DotaParser.link_1pos_position, mess=mess)
    await callback.message.edit_text(answer, reply_markup=cmd_start_keyboard)

@router.callback_query(F.data == '2_position')
async def cmd_2_position(callback: CallbackQuery):
    mess = "🏹 Мид"
    answer = get_answer(link=DotaParser.link_2pos_position, mess=mess)
    await callback.message.edit_text(answer, reply_markup=cmd_start_keyboard)

@router.callback_query(F.data == '3_position')
async def cmd_3_position(callback: CallbackQuery):
    mess = "🛡 Хардлайн"
    answer = get_answer(link=DotaParser.link_3pos_position, mess=mess)
    await callback.message.edit_text(answer, reply_markup=cmd_start_keyboard)

@router.callback_query(F.data == '4_position')
async def cmd_4_position(callback: CallbackQuery):
    mess = "🫴 Саппорт"
    answer = get_answer(link=DotaParser.link_4pos_position, mess=mess)
    await callback.message.edit_text(answer, reply_markup=cmd_start_keyboard)

@router.callback_query(F.data == '5_position')
async def cmd_5_position(callback: CallbackQuery):
    mess = "⚜️ Хард Саппорт"
    answer = get_answer(link=DotaParser.link_5pos_position, mess=mess)
    await callback.message.edit_text(answer, reply_markup=cmd_start_keyboard)