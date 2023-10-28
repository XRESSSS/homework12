import sqlite3

with sqlite3.connect('homework22.sqlite3') as connection:
    cursor = connection.cursor()

    # query = """
    #     CREATE TABLE IF NOT EXISTS books_shop(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         title TEXT NOT NULL,
    #         price INTEGER NOT NULL CHECK (price > 0),
    #         number_of_pages INTEGER NOT NULL CHECK (number_of_pages > 0)
    #     )
    # """
    # cursor.execute(query)

    # id = '1'
    # title = 'History'
    # price = 120
    # number_of_pages = 274
    # values = [id, title, price, number_of_pages]
    #
    # query = """
    #     INSERT INTO books_shop(id ,title, price, number_of_pages)
    #     VALUES (?, ?, ?, ?)
    # """
    # cursor.execute(query, values)

    # id = '2'
    # title = 'non-fiction'
    # price = 87
    # number_of_pages = 77
    # values = [id, title, price, number_of_pages]
    #
    # query = """
    #     INSERT INTO books_shop(id, title, price, number_of_pages)
    #     VALUES (?, ?, ?, ?)
    # """
    # cursor.execute(query, values)

    # values = (
    #     ('3', 'Geometry', 50, 600),
    #     ('4', 'History Ukraine', 99, 50),
    #     ('5', 'Literature', 250, 125),
    # )
    #
    # query = """
    #     INSERT INTO books_shop(id, title, price, number_of_pages)
    #     VALUES (?, ?, ?, ?)
    # """
    # cursor.executemany(query, values)

    # query = """
    #     SELECT title, price
    #     FROM books_shop
    #     WHERE price > 100
    # """
    # res = cursor.execute(query)
    # print(res.fetchmany(size=3))

    # query = """
    #     SELECT title, price
    #     FROM books_shop
    #     WHERE price
    #     ORDER BY price ASC
    #     LIMIT 3
    # """
    # res = cursor.execute(query)
    # print(res.fetchmany(size=10))

    # query = """
    #     SELECT title
    #     FROM books_shop
    #     WHERE title LIKE 'history%'
    #     LIMIT 2
    # """
    # res = cursor.execute(query)
    # print(res.fetchmany(size=10))

    # query = """
    #     ALTER TABLE books_shop
    #     ADD COLUMN barcode TEXT
    # """
    # cursor.execute(query)

    # query = """
    #     UPDATE books_shop
    #     SET
    #         barcode = :Barcode
    #     WHERE
    #         number_of_pages > 200
    # """
    # cursor.execute(query, {'Barcode': '0-00045'})

    # query = """
    #     DELETE FROM books_shop
    #     WHERE price = 100
    # """
    # cursor.execute(query)


