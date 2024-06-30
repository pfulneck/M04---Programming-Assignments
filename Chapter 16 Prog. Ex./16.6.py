# 16.6

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
SELECT title FROM books ORDER BY title
''')

for row in cursor.fetchall():
    print(row[0])

conn.close()