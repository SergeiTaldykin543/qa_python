import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture
    def collector_with_data(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Ну погоди')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Ну погоди', 'Мультфильмы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Ну погоди')
        return collector


    @pytest.fixture
    def empty_collector(self):
        return BooksCollector()

    def test_add_new_book_adds_one_book(self, empty_collector):
        empty_collector.add_new_book('Книга 1')
        assert len(empty_collector.get_books_genre()) == 1

    def test_add_new_book_adds_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        assert len(collector.get_books_genre()) == 3

    def test_add_new_book_cannot_add_same_book_twice(self, empty_collector):
        empty_collector.add_new_book('Ревизор')
        empty_collector.add_new_book('Ревизор')
        assert len(empty_collector.get_books_genre()) == 1


    @pytest.mark.parametrize('long_name',
        ['Очень длинное название книги которое больше сорока символов',
        'Ещё одно очень длинное название для теста'])

    def test_add_new_book_cannot_add_long_names(self, empty_collector, long_name):
        empty_collector.add_new_book(long_name)
        assert len(empty_collector.get_books_genre()) == 0

    def test_set_book_genre_sets_correct_genre(self, collector_with_data):
        collector_with_data.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector_with_data.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Комедии'

    def test_set_book_genre_cannot_set_wrong_genre(self, collector_with_data):
        collector_with_data.set_book_genre('Гордость и предубеждение и зомби', 'Приключения')
        assert collector_with_data.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_cannot_set_for_missing_book(self, empty_collector):
        empty_collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in empty_collector.get_books_genre()

    def test_get_book_genre_returns_correct_genre(self, collector_with_data):
        genre = collector_with_data.get_book_genre('Гордость и предубеждение и зомби')
        assert genre == 'Фантастика'

    def test_get_book_genre_returns_empty_for_no_genre(self, empty_collector):
        empty_collector.add_new_book('Книга без жанра')
        genre = empty_collector.get_book_genre('Книга без жанра')
        assert genre == ''

    def test_get_book_genre_returns_none_for_missing_book(self, empty_collector):
        genre = empty_collector.get_book_genre('Нет такой книги')
        assert genre is None

    def test_get_books_with_specific_genre_finds_fantasy_books(self, collector_with_data):
        books = collector_with_data.get_books_with_specific_genre('Фантастика')
        assert len(books) == 1
        assert 'Гордость и предубеждение и зомби' in books

    def test_get_books_with_specific_genre_finds_horror_books(self, collector_with_data):
        books = collector_with_data.get_books_with_specific_genre('Ужасы')
        assert len(books) == 1
        assert 'Что делать, если ваш кот хочет вас убить' in books

    def test_get_books_with_specific_genre_returns_empty_for_wrong_genre(self, collector_with_data):
        books = collector_with_data.get_books_with_specific_genre('Детективы')
        assert books == []

    def test_get_books_for_children_includes_child_friendly_books(self, collector_with_data):
        children_books = collector_with_data.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' in children_books
        assert 'Ну погоди' in children_books

    def test_get_books_for_children_excludes_adult_books(self, collector_with_data):
        children_books = collector_with_data.get_books_for_children()
        assert 'Что делать, если ваш кот хочет вас убить' not in children_books

    def test_get_books_for_children_excludes_books_without_genre(self, empty_collector):
        empty_collector.add_new_book('Книга без жанра')
        children_books = empty_collector.get_books_for_children()
        assert children_books == []

    def test_add_book_in_favorites_adds_book(self, collector_with_data):
        collector_with_data.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in collector_with_data.get_list_of_favorites_books()

    def test_add_book_in_favorites_cannot_add_twice(self, collector_with_data):
        initial_count = len(collector_with_data.get_list_of_favorites_books())
        collector_with_data.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector_with_data.get_list_of_favorites_books()) == initial_count

    def test_add_book_in_favorites_cannot_add_missing_book(self, empty_collector):
        empty_collector.add_book_in_favorites('Нет такой книги')
        assert len(empty_collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_removes_book(self, collector_with_data):
        collector_with_data.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector_with_data.get_list_of_favorites_books()

    def test_delete_book_from_favorites_does_nothing_for_missing_book(self, collector_with_data):
        initial_favorites = collector_with_data.get_list_of_favorites_books().copy()
        collector_with_data.delete_book_from_favorites('Нет такой книги')
        assert collector_with_data.get_list_of_favorites_books() == initial_favorites

    def test_delete_book_from_favorites_works_with_empty_list(self, empty_collector):
        empty_collector.delete_book_from_favorites('Любая книга')
        assert len(empty_collector.get_list_of_favorites_books()) == 0

    # Тесты для метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_returns_favorites(self, collector_with_data):
        favorites = collector_with_data.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in favorites
        assert 'Ну погоди' in favorites
        assert len(favorites) == 2

    def test_get_list_of_favorites_books_returns_empty_list(self, empty_collector):
        favorites = empty_collector.get_list_of_favorites_books()
        assert favorites == []

    def test_get_list_of_favorites_books_returns_copy(self, collector_with_data):
        original_favorites = collector_with_data.get_list_of_favorites_books()
        original_favorites_copy = original_favorites.copy()
        favorites = collector_with_data.get_list_of_favorites_books()
        favorites.append('Новая книга')

        assert 'Новая книга' in favorites
        current_favorites = collector_with_data.get_list_of_favorites_books()
        if len(current_favorites) == len(original_favorites_copy):
            assert current_favorites == original_favorites_copy
            assert 'Новая книга' not in current_favorites
        else:
            assert 'Новая книга' in current_favorites
            assert len(current_favorites) == len(original_favorites_copy) + 1
