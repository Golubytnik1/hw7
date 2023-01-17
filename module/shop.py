from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton("Оружие"),
    KeyboardButton("Снаряжение")
)


async def shop_start(cb: types.CallbackQuery):
    """
        Функция показывает категории
        Выбор с помощью кнопок
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Что вы хотите приобрести?",
        reply_markup=shop_kb
    )