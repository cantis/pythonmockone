import os
from dotenv import load_dotenv
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book, create_tables

load_dotenv()

host = os.getenv('POSTGRES_HOST')
username = os.getenv('POSTGRES_USERNAME')
password = os.getenv('POSTGRES_PASSWORD')
database = os.getenv('POSTGRES_DATABASE')

# set the PostgreSQL connection string
db_url = f'postgresql://{username}:{password}@localhost:5432/{database}'

# connect to the PostgreSQL database
engine = create_engine(db_url)

# check if the tables exist, if not create them
create_tables(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Check if the tables are empty, if so add some data
if session.query(Book).count() == 0:
    # Add books to the database
    book_list = []
    book_list.append(Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", pages=224, published="1979-10-12"))
    book_list.append(Book(title="The Restaurant at the End of the Universe", author="Douglas Adams", pages=160, published="1980-10-12"))
    book_list.append(Book(title="Life, the Universe and Everything", author="Douglas Adams", pages=224, published="1982-10-12"))
    book_list.append(Book(title="So Long, and Thanks for All the Fish", author="Douglas Adams", pages=224, published="1984-10-12"))
    book_list.append(Book(title="Mostly Harmless", author="Douglas Adams", pages=224, published="1992-10-12"))
    for book in book_list:
        session.add(book)
        session.commit()


def book_query() -> List[Book]:
    return session.query(Book).all()


def main() -> None:
    for book in book_query():
        print(book)

if __name__ == '__main__':
    main()

