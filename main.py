#TeleShell Bot v0.03 BETA
#Simple shell Executor telegram bot writen with aiogram(Python Lib) 
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("TeleShell BETA v0.03\nmade with <3")

@dp.message_handler()
async def echo(message: types.Message):
    try:
        result_record = os.system("%s > temp.result" % message.text)
        result = open("temp.result", "r+").read()
        await message.answer(result)
    except:
        await message.answer(message.text+" commend,\n Has failed.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
