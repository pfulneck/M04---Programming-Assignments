# 16.7

import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
SELECT * FROM books ORDER BY year
''')

for row in cursor.fetchall():
    print(row)

conn.close()