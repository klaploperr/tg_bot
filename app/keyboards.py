from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

article = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Забрать статью',
    url='https://teletype.in/@ilyaa.tar/qYqd_FHYD_M')]
])

questions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Забрать список',
    url='https://teletype.in/@ilyaa.tar/sEGUSnuUDii')]
])

form = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отбор на обучение',
    url='https://docs.google.com/forms/d/e/1FAIpQLScS2DkJ94Pg8lQw1s4vE6F_v4imtXprZ3GqIp92kTygYgiB5A/viewform?usp=header')]
])

demo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='База знаний DevOps',
    url='https://drive.google.com/drive/folders/11cUGHjbvPlQwkOJecjvVDcJ7eTYcZnYZ?usp=sharing')]
])

def sale_button(url):
    return InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплата',
    url=f'{url}')],
    #[InlineKeyboardButton(text='FAQ',
    #callback_data='FAQ')],
    [InlineKeyboardButton(text='Задать вопроос',
    url='https://t.me/ilyaa_tar')]
])


