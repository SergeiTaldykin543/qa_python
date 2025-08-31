import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_adds_one_book(self, empty_collector):
        empty_collector.add_new_book('Книга 1')
        assert len(empty_collector.get_books_genre()) == 1
        assert 'Книга 1' in empty_collector.books_genre
        assert empty_collector.books_genre['Книга 1'] == ''

    def test_add_new_book_adds_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        assert len(collector.get_books_genre()) == 3
        assert all(book in collector.books_genre for book in ['Книга 1', 'Книга 2', 'Книга 3'])

    def test_add_new_book_cannot_add_same_book_twice(self, empty_collector):
        empty_collector.add_new_book('Ревизор')
        empty_collector.add_new_book('Ревизор')
        assert len(empty_collector.get_books_genre()) == 1
        assert 'Ревизор' in empty_collector.books_genre

    @pytest.mark.parametrize('long_name', [
        'Очень длинное название книги которое больше сорока символов',
        'Ещё одно очень длинное название для теста'
    ])
    def test_add_new_book_cannot_add_long_names(self, empty_collector, long_name):
        empty_collector.add_new_book(long_name)
        assert len(empty_collector.get_books_genre()) == 0

    def test_set_book_genre_sets_correct_genre(self, collector_with_data):
        collector_with_data.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector_with_data.books_genre['Что делать, если ваш кот хочет вас убить'] == 'Комедии'

    def test_set_book_genre_cannot_set_wrong_genre(self, collector_with_data):
        collector_with_data.set_book_genre('Гордость и предубеждение и зомби', 'Приключения')
        assert collector_with_data.books_genre['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_set_book_genre_cannot_set_for_missing_book(self, empty_collector):
        empty_collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in empty_collector.books_genre

    def test_get_book_genre_returns_correct_genre(self, collector_with_data):
        genre = collector_with_data.get_book_genre('Гордость и предубеждение и зомби')
        assert genre == 'Фантастика'

    def test_get_book_genre_returns_empty_for_no_genre(self, collector_with_data):
        genre = collector_with_data.get_book_genre('Книга без жанра')
        assert genre == ''

    def test_get_book_genre_returns_none_for_missing_book(self, empty_collector):
        genre = empty_collector.get_book_genre('Нет такой книги')
        assert genre is None

    def test_get_books_with_specific_genre_finds_fantasy_books(self, collector_with_data):
        books = collector_with_data.get_books_with_specific_genre('Фантастика')
        assert books == ['Гордость и предубеждение и зомби']

    def test_get_books_with_specific_genre_finds_horror_books(self, collector_with_data):
        books = collector_with_data.get_books_with_specific_genre('Ужасы')
        assert books == ['Что делать, если ваш кот хочет вас убить']

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

    def test_get_books_for_children_excludes_books_without_genre(self, collector_with_data):
        children_books = collector_with_data.get_books_for_children()
        assert 'Книга без жанра' not in children_books

    def test_add_book_in_favorites_adds_book(self, collector_with_data):
        collector_with_data.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in collector_with_data.favorites

    def test_add_book_in_favorites_cannot_add_twice(self, collector_with_data):
        initial_count = len(collector_with_data.favorites)
        collector_with_data.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector_with_data.favorites) == initial_count

    def test_add_book_in_favorites_cannot_add_missing_book(self, empty_collector):
        empty_collector.add_book_in_favorites('Нет такой книги')
        assert len(empty_collector.favorites) == 0

    def test_delete_book_from_favorites_removes_book(self, collector_with_data):
        collector_with_data.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector_with_data.favorites

    def test_delete_book_from_favorites_does_nothing_for_missing_book(self, collector_with_data):
        initial_favorites = collector_with_data.favorites.copy()
        collector_with_data.delete_book_from_favorites('Нет такой книги')
        assert collector_with_data.favorites == initial_favorites

    def test_delete_book_from_favorites_works_with_empty_list(self, empty_collector):
        empty_collector.delete_book_from_favorites('Любая книга')
        assert len(empty_collector.favorites) == 0

    def test_get_books_genre_returns_all_books(self, collector_with_data):
        books_genre = collector_with_data.get_books_genre()
        expected = {
            'Гордость и предубеждение и зомби': 'Фантастика',
            'Что делать, если ваш кот хочет вас убить': 'Ужасы',
            'Ну погоди': 'Мультфильмы',
            'Книга без жанра': ''
        }
        assert books_genre == expected

    def test_get_books_genre_returns_empty_dict(self, empty_collector):
        books_genre = empty_collector.get_books_genre()
        assert books_genre == {}

    def test_get_books_genre_returns_reference_not_copy(self, collector_with_data):
        # Тестируем, что метод возвращает ссылку, а не копию
        returned_books = collector_with_data.get_books_genre()
        returned_books['Новая книга'] = 'Фантастика'

        # Оригинальный словарь должен измениться (так как возвращается ссылка)
        current_books = collector_with_data.get_books_genre()
        assert 'Новая книга' in current_books
        assert current_books['Новая книга'] == 'Фантастика'

    def test_get_list_of_favorites_books_returns_favorites(self, collector_with_data):
        favorites = collector_with_data.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in favorites
        assert 'Ну погоди' in favorites
        assert len(favorites) == 2

    def test_get_list_of_favorites_books_returns_empty_list(self, empty_collector):
        favorites = empty_collector.get_list_of_favorites_books()
        assert favorites == []

    def test_get_list_of_favorites_books_returns_reference_not_copy(self, collector_with_data):
        # Тестируем, что метод возвращает ссылку, а не копию
        returned_list = collector_with_data.get_list_of_favorites_books()
        returned_list.append('Новая книга')

        # Оригинальный список должен измениться (так как возвращается ссылка)
        current_favorites = collector_with_data.get_list_of_favorites_books()
        assert 'Новая книга' in current_favorites
        assert len(current_favorites) == 3