from aiogram import Bot,Dispatcher
from  aiogram import types
from aiogram.utils import executor

TOKEN = "5687627682:AAGhdtcDP4UdFwbduh_dc5p2o4i51YvDmM0"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

