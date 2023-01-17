from aiogram import types
from module.constans import COMMON_SWORD, BULAVA
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_weapon_kb = InlineKeyboardMarkup()
buy_weapon_kb.add(
    InlineKeyboardButton("Приобрести", callback_data="buy_weapon")
)


async def weapon_command(message: types.Message):
    """
        Функция показывает список оружия у Арно
    """
    await message.answer(text="Взгляни на эти мечи:")
    await message.answer(text=COMMON_SWORD, reply_markup=buy_weapon_kb)
    await message.answer(text=BULAVA, reply_markup=buy_weapon_kb)