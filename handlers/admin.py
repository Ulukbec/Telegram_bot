from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import bot, dp, ADMINS

from states.admin import ShopItemFSMAdmin
from db import sqlite_db


async def create_shop_item(message: types.Message):
    if message.from_user.id in ADMINS:
        await ShopItemFSMAdmin.title.set()
        await message.answer('Send item title')
    else:
        await message.answer('You are not admin')


async def set_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await message.answer('Send item image')
    await ShopItemFSMAdmin.next()


async def set_image(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['image'] = message.photo[0].file_id
    await ShopItemFSMAdmin.next()
    await message.answer('Send item price')


async def set_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)
        await ShopItemFSMAdmin.next()
        await message.answer('Select Item Category',
                             reply_markup=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(
                                 KeyboardButton('Телефоны'), KeyboardButton('Бытовая Техника'), KeyboardButton('Гаджеты')
                             ))
    except:
        await message.answer('Цена должна состоять только из цифр')


async def set_category(message: types.Message, state: FSMContext):
    if message.text == 'Телефоны' or message.text == 'Бытовая Техника' or message.text == 'Гаджеты':
        async with state.proxy() as data:
            data['category'] = message.text
        await sqlite_db.sql_add_command(state)
        await state.finish()
        await message.answer('Готово!')
    else:
        await message.answer('Wrong category name')
        await message.answer('Select Category Again',
                             reply_markup=ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(
                                 KeyboardButton('Телефоны'), KeyboardButton('Бытовая Техника'),
                                 KeyboardButton('Гаджеты')
                             ))


async def cancel_reg(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Да пошел ты')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_reg, Text(contains='CANCEL'), state='*')
    dp.register_message_handler(create_shop_item, commands=['reg'])
    dp.register_message_handler(set_title, state=ShopItemFSMAdmin.title)
    dp.register_message_handler(set_image, content_types=['photo'], state=ShopItemFSMAdmin.image)
    dp.register_message_handler(set_price, state=ShopItemFSMAdmin.price)
    dp.register_message_handler(set_category, state=ShopItemFSMAdmin.category)