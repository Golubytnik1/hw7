from aiogram import types
from module.constans import ARNO_INFO


async def arno(message: types.Message):
    """
        Функция для знакомства с ботом
    """
    await message.answer(text=ARNO_INFO)
    await message.delete()