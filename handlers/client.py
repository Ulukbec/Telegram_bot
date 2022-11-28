from aiogram import types
from aiogram import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards.client.info import categories
from db import sqlite_db


async def start_command(message: types.Message):
    await message.answer('Привет!', reply_markup=InlineKeyboardMarkup().add(
        InlineKeyboardButton('адрес магазина', callback_data='shop_address_call'),
        InlineKeyboardButton('Список категорий', callback_data='category_list_call')))


async def get_items_on_category(message: types.Message):
    if message.text == '/appliances':
        category_title = 'Бытовая Техника'
    elif message.text == '/phones':
        category_title = 'Телефоны'
    else:
        category_title = 'Гаджеты'
    items = await sqlite_db.sql_get_category_command(category_title)
    for item in items:
        await bot.send_photo(message.chat.id, photo=item[1], caption=f'{item[0]}\nPrice:{item[2]}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(get_items_on_category, commands=['appliances', 'phones', 'gadgets'])
