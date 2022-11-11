from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.utils import executor

TOKEN = "5687627682:AAGhdtcDP4UdFwbduh_dc5p2o4i51YvDmM0"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_comm(message: types.Message):
    me_bot = await bot.get_me()
    await message.answer(f"вас приветствует {me_bot.first_name}")


@dp.message_handler(commands=['help'])
async def help_comm(message: types.Message):
    await message.answer(f'/my_info - выводит id, first_name,last_name \n'
                         f'/download_photo - скачивает аватарку пользователя и открывает этот файл \n'
                         f'/show_movies - бот отправляет список фильмов с их названиями и ссылкой на сайтс этим фильмами \n'
                         f'/send_my_info - пользователь пишет свое имя, фамилия,возраст, чем занимается и список любимых фильмов или сериалов и бот группирует это в таком сообщении')


@dp.message_handler(commands=['my_info'])
async def my_info(messege: types.Message):
    await messege.answer(f'{messege.from_user.first_name} {messege.from_user.last_name}, {messege.from_id}')


@dp.message_handler(commands=['show_movies'])
async def movies(message: types.Message):
    await message.answer(f'/DEADPOOL_2\n/SONIK_2\n/SMILE')


@dp.message_handler(commands=['DEADPOOL_2'])
async def movies(message: types.Message):
    await message.answer('https://kinogo.zone/films/695-dedpul-2-hdtv2-v38.html')


@dp.message_handler(commands=['SONIK_2'])
async def movies(message: types.Message):
    await message.answer('https://kinogo.zone/films-2019/637-sonik-v-kino-2020-hdtv-v47.html')


@dp.message_handler(commands=['SMILE'])
async def movies(message: types.Message):
    await message.answer('https://kinogo.zone/films/16464-ulybka-2022-hd-v2.html')


#
# @dp.message_handler(commands=["send_my_info"])
# async def weather(message: types.Message):
#     await bot.send_message(message.from_user.id, "город")


@dp.message_handler(commands=['download_photo'])
async def photo(message: types.Message):
    photos = await bot.get_user_profile_photos(message.from_user.id)
    await bot.get_file(photos['photos'][0][0]['file_id'])
    await bot.send_photo(message.chat.id['photos'][0][0]['file_id'])


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
