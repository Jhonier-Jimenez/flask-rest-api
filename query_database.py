import sqlite3
conn = sqlite3.connect("books.db")
cur = conn.cursor()
cur.execute("SELECT * FROM author")


books = cur.fetchall()
for book in books:
    print(book)

cur.execute("PRAGMA table_info(author)")
columns_info = cur.fetchall()
for column in columns_info:
    print(column)