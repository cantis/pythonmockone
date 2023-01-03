import pytest

from app.core import main
from app.core.models import Book


def test_main(mocker):
    # arrange
    hobbit = Book(title="The Hobbit", author="J.R.R. Tolkien", pages=295, published="1937-09-21")
    mocker.patch("app.core.main.book_query", return_value=[hobbit])

    # act
    result = main.book_query()

    # assert
    assert result[0].title == "The Hobbit"
