# 16.2

import csv

with open('books.csv', 'r') as file:
    reader = csv.DictReader(file)
    books = list(reader)

for book in books:
    print(book)