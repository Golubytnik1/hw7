import sqlite3
from pathlib import Path


def init():
    """
        Функция для создания файла sqlite3
    """
    DB_NAME = "db.sqlite3"  # *'.db', '*.sqlite' - другие расширения
    DB_PATH = Path(__file__).parent.parent
    global db, cur
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cur = db.cursor()


def create_tables():
    """
        Функция для создания таблиц
    """
    cur.execute(
        """CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            descr TEXT,
            price INTEGER,
            photo TEXT)
        """
    )
    cur.execute(
        """CREATE TABLE IF NOT EXISTS orders (
                orders_id INTEGER PRIMARY KEY,
                user_name TEXT,
                address INTEGER,
                week_day TEXT,
                product_id INTEGER,
                FOREIGN KEY (product_id)
                    REFERENCES product (product_id)
                    ON DELETE CASCADE)
        """
    )
    db.commit()


def populate_products():
    """
        Функция для заполнения таблицы
    """
    cur.execute("""INSERT INTO products (
        name,
        descr,
        price,
        photo
    ) VALUES
    ('Кузнец Старк', 'Фантастика', 799, './images/1013809628.jpg'),
    ('Анчелотти', 'Романтика', 1199, './images/1013809628.jpg'),
    ('Восходящая звезда', 'Боевик', 699, './images/1013809628.jpg')
    """)
    db.commit()


def get_products():
    """
        Функция чтобы достать данные из таблицы по страницам
    """
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()


def order_process(data):
    """
        Фунцкия для заполнения order
    """
    data = data.as_dict()
    cur.execute("""INSERT INTO orders(
        username,
        address,
        product_id
    ) VALUES (:user_name,:address,:product_id)""",
                {'username': data['name'],
                 'address': data['address'],
                 'product_id': data['product_id']})
    db.commit()