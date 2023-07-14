# TELESHELL BOT v0.09:
# Simple shell Executor telegram bot writen with aiogram(Python Lib).
from aiogram import Bot, Dispatcher, executor, types
import os, sys
import tempfile

# CONFIG:
API_TOKEN = '' #<<< Set your bot's API token Here >>>
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
temp = tempfile.NamedTemporaryFile(prefix="TeleShell_", mode='w+')

# CODE:
@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("TeleShell BETA v0.09\nmade with <3")
@dp.message_handler()
async def echo(message: types.Message):
    try:
        session = await message.answer(message.text+" commend,\n START...<3")
        with os.popen(message.text) as process:
            for line in process:
                temp.write(line)
                temp.seek(0)
                await session.edit_text(temp.read())
    except:
        await session.edit_text(message.text+" commend,\n FAILED!</3")
    finally:
        temp.truncate(0)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
