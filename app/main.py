import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import psycopg2

from models import Book, Base

load_dotenv()

username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DATABASE")

posgres_url = f"postgres+psycopg2://{username}:{password}@localhost:5432/{database}"

engine = create_engine(posgres_url)

Base.metadata.create_all(engine)


def dependant_value() -> int:
    return 48


def main() -> None:
    print(dependant_value())


if __name__ == "__main__":
    main()
