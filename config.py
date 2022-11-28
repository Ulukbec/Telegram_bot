from aiogram import Bot, Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = '5845360526:AAGqTFkVzsQ0WrF1iAyfLEjoxNOKVthEIJ4'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = [1880076265]