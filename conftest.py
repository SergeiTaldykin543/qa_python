import pytest
from main import BooksCollector

@pytest.fixture
def collector_with_data():
    collector = BooksCollector()
    collector.books_genre = {
        'Гордость и предубеждение и зомби': 'Фантастика',
        'Что делать, если ваш кот хочет вас убить': 'Ужасы',
        'Ну погоди': 'Мультфильмы',
        'Книга без жанра': ''
    }
    collector.favorites = ['Гордость и предубеждение и зомби', 'Ну погоди']
    return collector

@pytest.fixture
def empty_collector():
    return BooksCollector()