from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class ShopItemFSMAdmin(StatesGroup):
    title = State()
    image = State()
    price = State()
    category = State()