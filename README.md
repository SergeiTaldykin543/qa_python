# qa_python 
# Тесты для метода add_new_book
- test_add_new_book_adds_one_book - проверяет добавление одной книги
- test_add_new_book_adds_multiple_books - проверяет добавление нескольких книг
- test_add_new_book_cannot_add_same_book_twice - проверяет, что нельзя добавить книгу дважды
- test_add_new_book_cannot_add_long_names - проверяет, что нельзя добавить книги с длинными названиями (>40 символов)

# Тесты для метода set_book_genre
- test_set_book_genre_sets_correct_genre - проверяет установку корректного жанра
- test_set_book_genre_cannot_set_wrong_genre - проверяет, что нельзя установить некорректный жанр
- test_set_book_genre_cannot_set_for_missing_book - проверяет, что нельзя установить жанр для отсутствующей книги

# Тесты для метода get_book_genre
- test_get_book_genre_returns_correct_genre - проверяет возврат корректного жанра
- test_get_book_genre_returns_empty_for_no_genre - проверяет возврат пустой строки для книги без жанра
- test_get_book_genre_returns_none_for_missing_book - проверяет возврат None для отсутствующей книги

# Тесты для метода get_books_with_specific_genre
- test_get_books_with_specific_genre_finds_fantasy_books - проверяет поиск книг по жанру "Фантастика"
- test_get_books_with_specific_genre_finds_horror_books - проверяет поиск книг по жанру "Ужасы"
- test_get_books_with_specific_genre_returns_empty_for_wrong_genre - проверяет возврат пустого списка для отсутствующего жанра

# Тесты для метода get_books_for_children
- test_get_books_for_children_includes_child_friendly_books - проверяет включение детских книг
- test_get_books_for_children_excludes_adult_books - проверяет исключение взрослых книг
- test_get_books_for_children_excludes_books_without_genre - проверяет исключение книг без жанра

# Тесты для метода add_book_in_favorites
- test_add_book_in_favorites_adds_book - проверяет добавление книги в избранное
- test_add_book_in_favorites_cannot_add_twice - проверяет, что нельзя добавить книгу в избранное дважды
- test_add_book_in_favorites_cannot_add_missing_book - проверяет, что нельзя добавить отсутствующую книгу в избранное

# Тесты для метода delete_book_from_favorites
- test_delete_book_from_favorites_removes_book - проверяет удаление книги из избранного
- test_delete_book_from_favorites_does_nothing_for_missing_book - проверяет, что удаление отсутствующей книги не меняет список
- test_delete_book_from_favorites_works_with_empty_list - проверяет работу с пустым списком избранного

# Тесты для метода get_list_of_favorites_books
- test_get_list_of_favorites_books_returns_favorites - проверяет возврат списка избранных книг
- test_get_list_of_favorites_books_returns_empty_list - проверяет возврат пустого списка
- test_get_list_of_favorites_books_returns_copy - проверяет, что возвращается копия списка

