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
    await message.answer_photo(open(
        './images/1641857001_51-gamerwall-pro-p-mantiya-volshebnika-fentezi-krasivo-foto-53.jpg', 'rb'),
        caption=MANTIYA, reply_markup=buy_armor_kb)
    await message.answer_photo(open('./images/255-HelmetDex7.png', 'rb'),
                               caption=BEAR_HEAD, reply_markup=buy_armor_kb)
