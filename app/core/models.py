import os
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Date, create_engine

base = declarative_base()

host = os.getenv('POSTGRES_HOST')
username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DATABASE")

# set the PostgreSQL connection string
db_url = f"postgresql://{username}:{password}@localhost:5432/{database}"
print(db_url)

# connect to the PostgreSQL database
engine = create_engine(db_url)


def create_tables(engine):
    '''Drop and create all tables'''
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


class Book(base):
    '''Represents a Book'''
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', pages='{self.pages}', published='{self.published}')>"
