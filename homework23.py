import sqlite3
from pprint import pprint

with sqlite3.connect('homework23_db.sqlite3') as connection:
    cursor = connection.cursor()

    # query = """
    #     CREATE TABLE IF NOT EXISTS author(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #     name TEXT NOT NULL
    #     )
    # """
    # cursor.execute(query)

    # query = """
    #     CREATE TABLE IF NOT EXISTS books(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #     title TEXT NOT NULL,
    #     author INTEGER,
    #     FOREIGN KEY (author) REFERENCES author(id)
    #     )
    # """
    # cursor.execute(query)

    # values = ['book', 3]
    # query = """
    #     INSERT INTO books(title, author)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)
    #
    # values = ['book', 3]
    # query = """
    #     INSERT INTO books(title, author)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)
    #
    # values = ['book', 3]
    # query = """
    #     INSERT INTO books(title, author)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)

    # values = [1, 'dsadsa']
    # query = """
    #     INSERT INTO author(id, name)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)
    # values = [3, 'jkhkjhkjhkjh']
    # query = """
    #       INSERT INTO author(id, name)
    #       VALUES(?, ?)
    #   """
    # cursor.execute(query, values)

    # query = """
    #     SELECT title, name
    #     FROM books
    #     JOIN author
    #     ON books.author = author.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())

    # query = """
    #     SELECT title, name
    #     FROM books
    #     LEFT JOIN author
    #     ON books.author = author.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())
    #
    # query = """
    #     SELECT title, name, author
    #     FROM books
    #     FULL JOIN author
    #     ON books.author = author.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())
