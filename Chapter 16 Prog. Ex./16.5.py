# 16.5

import csv
import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

with open('books2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
        ''', (row['title'], row['author'], row['year']))

conn.commit()
conn.close()