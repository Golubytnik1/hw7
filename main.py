# 17.01.2023
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
import logging
from module.start import start_command
from module.help import help_command
from module.arno_info import arno
from module.shop import shop_start
from module.weapon import weapon_command
from module.armor import armor_command


load_dotenv()
bot = Bot(getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(getenv("BOT_TOKEN"))
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(arno, commands=["arno"])
    dp.register_callback_query_handler(shop_start, text="shop_start")
    dp.register_message_handler(weapon_command, Text(equals="Оружие"))
    dp.register_message_handler(armor_command, Text(equals="Снаряжение"))

    executor.start_polling(dp, skip_updates=True)