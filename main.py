#TeleShell Bot v0.08 BETA
#Simple shell Executor telegram bot writen with aiogram(Python Lib) 
from aiogram import Bot, Dispatcher, executor, types
import os, sys
import tempfile

API_TOKEN = '' #<<< Set your bot's API token Here >>>
PROXY_URL = '' #<<< Set your bot's Proxy Here >>>

bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)
temp = tempfile.NamedTemporaryFile(prefix="TeleShell_")

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("TeleShell BETA v0.08\nmade with <3")

@dp.message_handler()
async def echo(message: types.Message):
    try:
        session = await message.answer(message.text+" commend,\n START...<3")
        result_record = os.system("%s > %s" % message.text, temp.name)
        result = open(temp.name, "r+").read()
        await session.edit_text(result)
    except:
        await session.edit_text(message.text+" commend,\n FAILED!</3")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
