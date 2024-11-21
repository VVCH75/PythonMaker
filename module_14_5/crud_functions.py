import sqlite3
from aiogram.filters.state import State, StatesGroup


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL,
    url TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
    connection.commit()
    connection.close()


def get_all_products():
    all_product = []
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    for product in products:
        all_product.append(product)
    connection.commit()
    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()
    connection.close()



def is_included(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        return False
    return True

initiate_db()