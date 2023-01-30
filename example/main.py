from aiogram import Bot, Dispatcher, executor, types

#бот - сервер который взаимодействует с API Telegramm
TOKEN_API = "5778379713:AAGQZMTKNrHv7IJ0DuBrjuOi-AYTkWje6S0"#Токен  бота

HELP_COMMAND = """ 
/help - список комманд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.message):
    await message.reply(HELP_COMMAND)
@dp.message_handler(commands=['start'])
async def help_command(message: types.message):
    await message.answer('Acces allowed')
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp)
