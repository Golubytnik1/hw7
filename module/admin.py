from aiogram import types


async def message_log(message: types.Message):
    """
        Функция для получения сведений о сообщениях в логах
    """
    print(f"{message.chat.type=}")
    print(f"{message.reply_to_message=}")
    print(f"{message.from_user.id=}")
    if message.chat.type != "private":
        admins = await message.chat.get_administrators()
        print(admins)


async def proverka_admin(message: types.Message):
    """
        Функция для проверки на права админа
    """
    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin["user"]["id"] == message.from_user.id:
            return True
        return False


async def bad_words(message: types.Message):
    """
        Функция для проверки использовования
        плохих слов в сообщении
    """
    bad_w = ["тупой", "неуч", "бездарь", "сука"]
    if message.chat.type != 'private':
        for word in bad_w:
            if message.text.lower().replace(' ', '').count(word):
                await message.reply(text=f'Этот наглец {message.from_user.first_name} сказал, то чего не стоило!\n'
                                         f'Отцы наказать {message.from_user.first_name}: да/нет')
                break


async def ban_user(message: types.Message):
    """
        Функция для бана пользовотале
        после упоминания админа ботом
        при использовование плохих слов
    """
    if message.chat.type != 'private':
        admin_author = await proverka_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )


async def da_net(message: types.Message):
    '''
        Функция обрабатывает ответы администраторов беседы и банит пользователя
    '''
    if message.chat.type != 'private':
        answer_admin = await proverka_admin(message)
        print(answer_admin)
        if answer_admin and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )