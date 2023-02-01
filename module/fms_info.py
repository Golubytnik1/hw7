from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from db.base import order_process


class Form(StatesGroup):
    product_id = State()
    username = State()
    address = State()
    done = State()


async def cancel_handler(message: types.Message, state: FSMContext):
    """
        Функция для отмены FSM
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply(
        'Отмена',
        reply_markup=types.ReplyKeyboardRemove())


async def form_start(cb: types.CallbackQuery, state: FSMContext):
    """
        Функция для старта FSM
    """
    await Form.product_id.set()
    async with state.proxy() as data:
        data['product_id'] = int(cb.data.replace('form_start ', ''))
    await Form.next()
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text="Введите ваше имя:"
    )


async def process_name(message: types.Message, state: FSMContext):
    """
        Обработчик первой функции и задаем второй вопрос
    """
    if not message.text.isalpha():
        await message.reply('Вводите только буквы!')
    else:
        async with state.proxy() as data:
            data['name'] = message.text

    await Form.next()
    await message.reply("Введите ваш адресс:")


async def process_address(message: types.Message, state: FSMContext):
    """
        Обработчик второй функции функции и задаем третий вопрос
    """
    async with state.proxy() as data:
        data['address'] = message.text

        yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        yes_no_kb.add(
            KeyboardButton("Да"),
            KeyboardButton("Нет")
        )

        await Form.next()
        await message.reply(f"""Подтвердите ваши данные:
            Имя: {data['name']}
            Адрес: {data['address']}
            Данные верны?
            """, reply_markup=yes_no_kb)


async def process_done(message: types.Message, state: FSMContext):
    """
        Функция для финиша
    """
    async with state.proxy() as data:
        order_process(data)

    await message.reply(
        "Благодарю за заполнение анкеты!",
        reply_markup=ReplyKeyboardRemove()
    )
