from aiogram import types
from aiogram import Dispatcher
from config import bot
from keyboards.client.info import categories


async def get_shop_address(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, text='Адрес: Ибраимова 103a')


async def get_category_list(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, text='Выберите категорию', reply_markup=categories)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(get_shop_address, lambda call: call.data == 'shop_address_call')
    dp.register_callback_query_handler(get_category_list, lambda call: call.data == 'category_list_call')
