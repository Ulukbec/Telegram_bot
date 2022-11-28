from aiogram import executor
from config import bot, dp
from handlers import client, callback, admin
from db import sqlite_db

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

async def on_startup(_):
    sqlite_db.sql_create()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
