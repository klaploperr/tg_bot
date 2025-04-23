from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

article = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Забрать статью',
    url='https://teletype.in/@ilyaa.tar/qYqd_FHYD_M')]
])

guide = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Забрать гайд',
    url='https://teletype.in/@ilyaa.tar/H5o3UAYL9GB')]
])

questions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Забрать список',
    url='https://teletype.in/@ilyaa.tar/KpCUtcNedid')]
])

form = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отбор на обучение',
    url='https://docs.google.com/forms/d/e/1FAIpQLScS2DkJ94Pg8lQw1s4vE6F_v4imtXprZ3GqIp92kTygYgiB5A/viewform?usp=header')]
])

demo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='База знаний DevOps',
    url='https://drive.google.com/drive/folders/11cUGHjbvPlQwkOJecjvVDcJ7eTYcZnYZ?usp=sharing')]
])

question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Задать вопрос',
    url='https://t.me/ilyaa_tar')]
    ])

async def sale_button(sale_url):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Оплата', url=f'{sale_url}'))
    return keyboard.adjust(1).as_markup()