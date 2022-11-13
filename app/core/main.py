import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# from app.models import Book, Base

load_dotenv()

username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DATABASE")

# set the postgres connection string
posgres_url = f"postgresql://{username}:{password}@localhost:5432/{database}"

# connect to the postgres database
engine = create_engine(posgres_url)

# Base.metadata.create_all(engine)


def dependant_value() -> int:
    return 48


def main() -> None:
    # temp =  Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", pages=224, published="1979-10-12")
    print(dependant_value())


if __name__ == "__main__":
    main()
