from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

HELP_COMMAND = """ 
Вот что я умею:

/couples -  Отправлять расписание пар ;
/bells   -  Отправлять расписание звонков ;
/glist   -  Отправлять список группы ;

Документация: ;

Для проверки работоспособности - /ping
"""

#Расписание звонков  -  https://sun9-19.userapi.com/impg/aVsOTHw2QWtLls5xidE2A21dITC_9izJY2KtEQ/FAZgXgzp7q0.jpg?size=798x309&quality=96&sign=323545e297a1c90f4412a0062b90620d&type=album
#Расписание пар  -  https://sun9-69.userapi.com/impg/DyQ4ppDaaOPnSTc2sLHyhN3_dEyhDF-WE2M0Mw/xc3HEVOKwBw.jpg?size=732x367&quality=96&sign=f71baa5c78fc8ac2ffe6843250377eff&type=album
#Список группы  -  https://sun9-77.userapi.com/impg/LBqkhz-5s3qdoo8vva8f0uYdLn3toZJHMRo1jw/XtAA7A35mII.jpg?size=223x569&quality=96&sign=91290bea775f9b3e96f7acf490c154e7&type=album


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
pingRequest = 2

# 
#  --------------- Стандартные комманды ---------------
#

@dp.message_handler(commands=['help'])
async def help_command(message: types.message):
    await message.reply(HELP_COMMAND)



@dp.message_handler(commands=['start'])
async def help_command(message: types.message):
    await message.answer('Для вывода списка доступных комманд - /help')
    await message.delete()

# 
#  --------------- Админ комманды ---------------
#

@dp.message_handler(commands='amenu')
async def amenu_command(message: types.message):
    if message.from_user.username == "asd":
        await message.answer(str(message.from_user.first_name)+' is admin')
    else:
        await message.answer('You isnt admin')



@dp.message_handler(commands='ping')
async def ping_command(message: types.message):
    if 2==pingRequest:
        await message.reply('Понг!')
    else:
        await message.reply('Что то не так работает')



@dp.message_handler(commands='tipidor')
async def pidor_option(message: types.message):
    if message.from_user.username == "kksihtk":
        await message.reply('Так точно хозяин')
    else:
        await message.reply('Иди нахуй')

# 
#  --------------- Юзер комманды ---------------
#

@dp.message_handler(commands='couples')
async def rp_command(message: types.message):
    await message.answer('Вот расписание 2-го семестра:')
    await bot.send_phot(chat_id=message.chat.id, photo='https://sun9-69.userapi.com/impg/DyQ4ppDaaOPnSTc2sLHyhN3_dEyhDF-WE2M0Mw/xc3HEVOKwBw.jpg?size=732x367&quality=96&sign=f71baa5c78fc8ac2ffe6843250377eff&type=album')

@dp.message_handler(commands='bells')
async def rp_command(message: types.message):
    await message.answer('Вот расписание звонков:')
    await bot.send_phot(chat_id=message.chat.id, photo='https://sun9-19.userapi.com/impg/aVsOTHw2QWtLls5xidE2A21dITC_9izJY2KtEQ/FAZgXgzp7q0.jpg?size=798x309&quality=96&sign=323545e297a1c90f4412a0062b90620d&type=album')

@dp.message_handler(commands='glist')
async def rp_command(message: types.message):
    await message.answer('Вот список группы:')
    await bot.send_phot(chat_id=message.chat.id, photo='https://sun9-77.userapi.com/impg/LBqkhz-5s3qdoo8vva8f0uYdLn3toZJHMRo1jw/XtAA7A35mII.jpg?size=223x569&quality=96&sign=91290bea775f9b3e96f7acf490c154e7&type=album')

# 
#  --------------- Конец ---------------
#

if __name__ == "__main__":
    executor.start_polling(dp)
