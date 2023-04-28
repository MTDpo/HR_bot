from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types.input_media import InputMediaVideo
import aiogram.types.input_media
import logging
from hr_keyboard import *
from hr_text import *
import config


# Debug mode
#logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG)


bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
user_dict = {}
hr_keyboard = Keyboard()
hr_text = text()

class User:
    def __init__(self, name):
        self.name = name
        self.telegram_id = None
        self.option = None
        self.parent = None


@dp.message_handler(lambda message: message.text == '/start' in message.text, content_types=['text'])
async def start_handler(message):
    chat_id = message.from_user.id
    name = message.from_user.id
    user = User(name)
    user_dict[chat_id] = user
    user.telegram_id = name
    user.parent = None
    await bot.send_message(message.from_user.id, hr_text.inlinetext(), reply_markup=hr_keyboard.inlinekey())


@dp.callback_query_handler(lambda c: c.data == 'back_button')
async def process_callback_button1(c):
    await bot.delete_message(c.message.chat.id, c.message.message_id)
    chat_id = c.from_user.id
    user = user_dict[chat_id]
    user.option = user.parent
    await bot.answer_callback_query(c.id)
    await bot.send_message(c.from_user.id, hr_text.inlinetext(),  reply_markup=hr_keyboard.inlinekey(option=user.parent))


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button1(c):
    await bot.delete_message(c.message.chat.id, c.message.message_id)
    chat_id = c.from_user.id
    user = user_dict[chat_id]
    if user.parent == None:
        user.parent = 'inline_btn_0'
    else:
        user.parent = user.option
    user.option = c.data
    print(user.parent, user.option)
    await bot.answer_callback_query(c.id)
    await bot.send_message(c.from_user.id, hr_text.inlinetext(option=user.option), reply_markup=hr_keyboard.inlinekey(option=user.option, parent=user.parent))


@dp.callback_query_handler(lambda c: c.data == 'inline_btn_0')
async def on_main_menu(c):
    await bot.delete_message(c.message.chat.id, c.message.message_id)
    chat_id = c.from_user.id
    user = user_dict[chat_id]
    await bot.answer_callback_query(c.id)
    await bot.send_message(c.from_user.id, hr_text.inlinetext(), reply_markup=hr_keyboard.inlinekey())








async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp)