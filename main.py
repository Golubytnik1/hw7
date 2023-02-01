# 17.01.2023
from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp

"""импорт хелпа, старта и инфо"""
from module.arno_info import arno
from module.help import help_command
from module.start import start_command

"""импорт функций магазина"""
from module.armor import armor_command
from module.books import show_books
from module.shop import shop_start
from module.weapon import weapon_command

"""импорт функций админ бота"""
from module.admin import bad_words, ban_user, da_net

"""импорт анкеты"""
from module.fms_info import (Form, cancel_handler, form_start, process_address,
                             process_done, process_name)

"""импорт базы данных"""
from db.base import create_tables, init


async def startup(_):
	"""
		Функция для запуска стронних сервисов
	"""
	init()
	create_tables()


#Регисторы БД и фмс анкетой
dp.register_callback_query_handler(process_name, Text(startswith='form_start'))
dp.register_message_handler(form_start, commands=['form'])
dp.register_message_handler(form_start, Text(equals='Нет'), state=Form.done)
dp.register_message_handler(cancel_handler, state='*', commands='cancel')
dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
dp.register_message_handler(process_name, state=Form.username)
dp.register_message_handler(process_address, state=Form.address)
dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
#Регистор для старта
dp.register_message_handler(start_command, commands=["start"])
#Регистор для помощи о всех командах
dp.register_message_handler(help_command, commands=["help"])
#Регистор про инфо о боте
dp.register_message_handler(arno, commands=["arno"])
#Регистор магазина
dp.register_callback_query_handler(shop_start, text="shop_start")
#Регистор магазина об оружии
dp.register_message_handler(weapon_command, Text(equals="Оружие"))
#Регистор магазина о снаряжении
dp.register_message_handler(armor_command, Text(equals="Снаряжение"))
#Регистор магазина о книгах
dp.register_message_handler(show_books, Text(equals="Книги о легендах"))
#Регистор кика пользователя
dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
#Регистор кика пользователя 	при ответе от админа !да
dp.register_message_handler(da_net, commands=['да'], commands_prefix=['!'])
#проверка употребление плохих слов
dp.register_message_handler(bad_words)


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True, on_startup=startup)