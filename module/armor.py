from aiogram import types
from module.constans import MANTIYA, BEAR_HEAD
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_armor_kb = InlineKeyboardMarkup()
buy_armor_kb.add(
    InlineKeyboardButton("Приобрести", callback_data="buy_armor")
)


async def armor_command(message: types.Message):
    """
        Функция показывает список снаряжения у Арно
    """
    await message.answer(text="Взгляни на это снаряжение:")
    await message.answer(text=MANTIYA, reply_markup=buy_armor_kb)
    await message.answer(text=BEAR_HEAD, reply_markup=buy_armor_kb)
