import pytest

from main import BooksCollector


@pytest.fixture()
def books():
    books = BooksCollector()
    return books
