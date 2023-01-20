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
    await message.answer_photo(open('./image/kXlUP-J6ManaSMZCJnOpJQ.jpeg', 'rb'),
                               caption=COMMON_SWORD, reply_markup=buy_weapon_kb)
    await message.answer_photo(open('./image/sn_104_1_004.jpg', 'rb'),
                               caption=BULAVA, reply_markup=buy_weapon_kb)