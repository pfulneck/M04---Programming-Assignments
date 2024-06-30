# 16.4

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE books (
    title TEXT,
    author TEXT,
    year INTEGER
               )
               ''')

conn.commit()
conn.close()