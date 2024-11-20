import sqlite3

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

initiate_db()