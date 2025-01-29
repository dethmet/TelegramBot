from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
],
                        resize_keyboard=True,
                        input_field_placeholder='Выберете пунк ниже')

sattings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/@dethmet')]
    ])

pidors = ['Elton', 'Baskov', 'Zelenskiy', 'Kirkorov', 'Galkin']

async def inline_pidors():
    keyboard = InlineKeyboardBuilder()
    for pidor in pidors:
        keyboard.add(InlineKeyboardButton(text=pidor, url='https://www.youtube.com/@dethmet'))
    return keyboard.adjust(4).as_markup()
