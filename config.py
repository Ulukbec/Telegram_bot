from aiogram import Bot, Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = '5601832863:AAHD7CT0_RKC82eWN9fu_Q4hXRdQNDd1CF8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = [1018470926]
