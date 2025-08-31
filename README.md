# qa_python 
# Тесты для метода add_new_book
- test_add_new_book_add_two_books - добавление двух книг
- test_add_new_book_adds_one_book - добавление одной книги
- test_add_new_book_adds_multiple_books - добавление нескольких книг
- test_add_new_book_cannot_add_same_book_twice - нельзя добавить книгу дважды
- test_add_new_book_cannot_add_long_names - нельзя добавить книгу с длинным названием (параметризованный)

# Тесты для метода set_book_genre
- test_set_book_genre_sets_correct_genre - установка корректного жанра
- test_set_book_genre_cannot_set_wrong_genre - нельзя установить некорректный жанр
- test_set_book_genre_cannot_set_for_missing_book - нельзя установить жанр несуществующей книге

# Тесты для метода get_book_genre
- test_get_book_genre_returns_correct_genre - возврат корректного жанра
- test_get_book_genre_returns_empty_for_no_genre - возврат пустого жанра
- test_get_book_genre_returns_none_for_missing_book - возврат None для несуществующей книги

# Тесты для метода get_books_with_specific_genre
- test_get_books_with_specific_genre_finds_fantasy_books - поиск книг по жанру "Фантастика"
- test_get_books_with_specific_genre_finds_horror_books - поиск книг по жанру "Ужасы"
- test_get_books_with_specific_genre_returns_empty_for_wrong_genre - пустой результат для некорректного жанра

# Тесты для метода get_books_for_children
- test_get_books_for_children_includes_child_friendly_books - включение детских книг
- test_get_books_for_children_excludes_adult_books - исключение взрослых книг
- test_get_books_for_children_excludes_books_without_genre - исключение книг без жанра

# Тесты для метода add_book_in_favorites
- test_add_book_in_favorites_adds_book - добавление книги в избранное
- test_add_book_in_favorites_cannot_add_twice - нельзя добавить книгу дважды в избранное
- test_add_book_in_favorites_cannot_add_missing_book - нельзя добавить несуществующую книгу

# Тесты для метода delete_book_from_favorites
- test_delete_book_from_favorites_removes_book - удаление книги из избранного
- test_delete_book_from_favorites_does_nothing_for_missing_book - ничего не делает для несуществующей книги
- test_delete_book_from_favorites_works_with_empty_list - работа с пустым списком

# Тесты для метода get_books_genre
- test_get_books_genre_returns_all_books - возврат всех книг
- test_get_books_genre_returns_empty_dict - возврат пустого словаря
- test_get_books_genre_returns_reference_not_copy - возврат ссылки, а не копии

# Тесты для метода get_list_of_favorites_books
- test_get_list_of_favorites_books_returns_favorites - возврат избранных книг
- test_get_list_of_favorites_books_returns_empty_list - возврат пустого списка
- test_get_list_of_favorites_books_returns_reference_not_copy - возврат ссылки, а не копии
