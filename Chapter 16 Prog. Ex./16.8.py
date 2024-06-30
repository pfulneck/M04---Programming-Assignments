# 16.8

from sqlalchemy import create_engine, Table, MetaData, select

engine = create_engine('sqlite:///books.db')
metadata = MetaData()
metadata.reflect(bind=engine)
books_table = metadata.tables['books']

with engine.connect() as conn:
    query = select([books_table.c.title]).order_by(books_table.c.title)
    result = conn.execute(query)
    for row in result:
        print(row['title'])