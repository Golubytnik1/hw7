from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


class Form(StatesGroup):
    name = State()
    age = State()
    day = State()
    done = State()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply(
        'Отмена',
        reply_markup=types.ReplyKeyboardRemove())


async def form_start(message: types.Message):
    """
        Функция для старта FMS
    """
    await Form.name.set()
    await message.reply("Введите ваше имя:")


async def process_name(message: types.Message, state: FSMContext):
    """
        Обработчик первой функции и задаем второй вопрос
    """
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)

    await Form.next()
    await message.reply("Введите ваш возраст:")


async def process_age(message: types.Message, state: FSMContext):
    """
        Обработчик второй функции и задаем третий вопрос
    """
    if not message.text.isdigit():
        await message.reply("Слушай парень, я думаю возраст пишется с помощью чисел ;)")
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        week_days_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        week_days_kb.add(
            KeyboardButton("Понедельник"),
            KeyboardButton("Вторник"),
            KeyboardButton("Среда"),
            KeyboardButton("Четверг"),
            KeyboardButton("Пятница")
        )
        await Form.next()
        await message.reply(
            "Выберите день недели для получения ответа от Арно:",
            reply_markup=week_days_kb
        )


async def process_day(message: types.Message, state: FSMContext):
    """
        Обработчик третьей функции
    """
    async with state.proxy() as data:
        data['day'] = message.text

    yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    yes_no_kb.add(
        KeyboardButton("Да"),
        KeyboardButton("Нет")
    )

    await Form.next()
    await message.reply(f"""Подтвердите ваши данные:
    Имя: {data['name']}
    Возраст: {data['age']}
    День получения ответа: {data['day']}
    Все верно?
    """, reply_markup=yes_no_kb)


async def process_done(message: types.Message, state: FSMContext):
    """
        Функция для финиша
    """
    await state.finish()
    await message.reply(
        "Благодарю за заполнение анкеты!",
        reply_markup=ReplyKeyboardRemove()
    )
