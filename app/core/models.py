import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date

base = declarative_base()


def create_tables(engine):
    base.metadata.create_all(engine)


class Book(base):
    '''Represents a Book'''

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)

    def __repr__(self):
        return f"title='{self.title}', author='{self.author}', pages='{self.pages}', published='{self.published}'"
