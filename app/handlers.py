
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                        reply_markup=await kb.inline_pidors())


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Бог помощь тебе /help')


@router.message(F.text == 'Как дела, братка?')
async def how_are_you(message: Message):
    await message.answer('Пока не родила. АХАХАХА')


@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://sun9-1.userapi.com/impf/Ls-1OT6a6X1FLnBSnXZKcV1FhRePPrGHzAIrQw/xQySqmfBtPU.jpg?size=700x607&quality=96&sign=bfc9558697717136c0b6aa620131248e&c_uniq_tag=eO7YMvdUZcUkgVCrDIT6Hb56sJBZOLhzkxIGKippHB8&type=album.jpg',
        caption='Это та крутая твоя фотка в лифте'
    )
    

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
