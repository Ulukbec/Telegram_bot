from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

categories = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

appliances = KeyboardButton('/appliances')
phones = KeyboardButton('/phones')
gadgets = KeyboardButton('/gadgets')

categories.add(appliances, phones, gadgets)