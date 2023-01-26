from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.base import get_products


def buy_books_kb(product_id):
    buy_books_kb = InlineKeyboardMarkup()
    buy_books_kb.add(InlineKeyboardButton("Приобрести", callback_data=f"buy_books"))
    return buy_books_kb


async def show_books(message: types.Message):
    """
        Функция показывает книги
    """
    await message.answer(text="Вот наши книги:")
    stark_book = get_products()[0]
    anchelotti_book = get_products()[1]
    stars_book = get_products()[2]

    await message.answer_photo(
        open(stark_book[4], 'rb'),
        caption=f'{stark_book[1]}, цена - {stark_book[3]}',
        reply_markup=buy_books_kb(stark_book)
    )

    await message.answer_photo(
        open(anchelotti_book[4], 'rb'),
        caption=f'{anchelotti_book[1]}, цена - {anchelotti_book[3]}',
        reply_markup=buy_books_kb(anchelotti_book)
    )

    await message.answer_photo(
        open(stars_book[4], 'rb'),
        caption=f'{stars_book[1]}, цена - {stars_book[3]}',
        reply_markup=buy_books_kb(stars_book)
    )