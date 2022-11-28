import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    if db:
        print('Connected successfully!')
        db.execute(
            "CREATE TABLE IF NOT EXISTS shopitem(title TEXT PRIMARY KEY, image TEXT, price INTEGER , category TEXT)")
        db.commit()


async def sql_add_command(state):
    insert_query = f'INSERT INTO shopitem VALUES (?, ?, ?, ?)'

    async with state.proxy() as data:
        cursor.execute(insert_query, tuple(data.values()))
        db.commit()


async def sql_get_category_command(category):
    select_query = f'SELECT * FROM shopitem WHERE category = ?'

    return cursor.execute(select_query, (category,))
