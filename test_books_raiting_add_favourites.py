import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_init_books_have_param_genre(self, books):
        assert books.books_genre == {}

    def test_init_genre__have_param_favorites(self, books):
        assert books.favorites == []

    def test_init__have_param_genre(self, books):
        expected_genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books.genre == expected_genre

    def test_init__have_param_genre_age_rating(self, books):
        expected_genre_age_rating = ['Ужасы', 'Детективы']
        assert books.genre_age_rating == expected_genre_age_rating

    @pytest.mark.parametrize(
        'name',
        [
            'С',
            'СЮ',
            'Дюна',
            'Краткое имя',
            'Еще одна книга',
            'Книга с названием длиной ровно тридцать',
            'Книга с названием длиной ровно сорок сим',
        ]
    )
    def test_add_new_book_positive_add_book_in_dict(self, books, name):
        books.add_new_book(name)
        assert name in books.books_genre

    @pytest.mark.parametrize(
        'name',
        [
            '',
            'Книга с названием длиной ровно сорок один',
            'Книга с названием длиной ровно сорок два с'
        ]
    )
    def test_add_new_book_neg_no_add_book_in_dict(self, books, name):
        books.add_new_book(name)
        assert name not in books.books_genre

    def test_add_new_book_duplicate_book_no_add_in_dict(self, books):
        books.add_new_book('Дюна')
        books.add_new_book('Дюна')
        assert len(books.books_genre) == 1

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Дюна', 'Фантастика'],
            ['Смешная книга', 'Комедии']
        ]
    )
    def test_set_book_genre_positive_add_genre(self, books, name, genre):
        books.add_new_book(name)
        books.set_book_genre(name, genre)
        assert books.books_genre[name] == genre

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Напалеон', 'Биография'],
            ['Железный человек 2024', 'Комикс']
        ]
    )
    def test_set_book_genre_neg_no_add_genre_in_dict(self, books, name, genre):
        books.add_new_book(name)
        books.set_book_genre(name, genre)
        assert books.books_genre[name] == ''

    @pytest.mark.parametrize(
        'name,genre',
        [
            ('Гарри Поттер', 'Фантастика'),
            ('Властелин Колец', 'Фантастика'),
            ('Игра престолов', 'Фантастика'),
            ('Пищеблок', 'Ужасы')
        ]
    )
    def test_get_books_with_specific_genre_show_book_choice_genre(self, books, name, genre):
        books_dict = {}
        for name, genre in [('Гарри Поттер', 'Фантастика'), ('Властелин Колец', 'Фантастика'), ('Игра престолов', 'Фантастика'), ('Пищеблок', 'Ужасы')]:
            books.add_new_book(name)
            books.set_book_genre(name, genre)
            books_dict[name] = genre
        assert books.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Властелин Колец', 'Игра престолов']

    def test_get_book_genre(self, books):
        books.add_new_book('Война и Мир')
        books.set_book_genre('Война и Мир', 'Детективы')
        assert books.books_genre['Война и Мир'] == 'Детективы'

    @pytest.mark.parametrize(
        'name,genre',
        [
            ('Лунтик', 'Мультфильмы'),
            ('Хоббит', 'Мультфильмы'),
            ('Приключения Незнайки', 'Фантастика'),
            ('Три богатыря', 'Комедии')
        ]
    )
    def test_get_books_for_children_positive_show_book_for_childs(self, books, name, genre):
        books_dict = {}
        for name, genre in [('Лунтик', 'Мультфильмы'), ('Хоббит', 'Мультфильмы'), ('Приключения Незнайки', 'Фантастика'), ('Три богатыря', 'Комедии')]:
            books.add_new_book(name)
            books.set_book_genre(name, genre)
            books_dict[name] = genre
        assert books.get_books_for_children() == ['Лунтик', 'Хоббит', 'Приключения Незнайки', 'Три богатыря']

    def test_get_books_for_children_neg_book_for_adult(self, books):
        books.add_new_book('Игра кальмара')
        books.set_book_genre('Игра кальмара', 'Ужасы')
        assert books.get_books_for_children() == []

    def test_add_book_in_favorites_positive_show_favotites_book(self, books):
        books.add_new_book('Дюна')
        books.set_book_genre('Дюна', 'Фантастика')
        books.add_book_in_favorites('Дюна')
        assert 'Дюна' in books.favorites

    def test_add_book_in_favorites_book_in_favorites(self, books):
        books.add_new_book('Дюна')
        books.set_book_genre('Дюна', 'Фантастика')
        books.add_book_in_favorites('Дюна')
        books.favorites.append('Дюна')
        assert list('Дюна') not in books.favorites

    def test_delete_book_from_favorites(self, books):
        books.add_new_book('Дюна')
        books.set_book_genre('Дюна', 'Фантастика')
        books.add_book_in_favorites('Дюна')
        books.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in books.favorites

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('1984', 'Фантастика'),
            ('Мастер и Маргарита', 'Фантастика'),
            ('Убить пересмешника', 'Детектив')
        ]
    )
    def test_get_list_of_favorites_books(self, books, name, genre):
        books_list = []
        for name, genre in [('1984', 'Фантастика'),
            ('Мастер и Маргарита', 'Фантастика'),
            ('Убить пересмешника', 'Детектив')]:
            books.add_new_book(name)
            books.set_book_genre(name, genre)
            books.add_book_in_favorites(name)
            books_list.append(name)
        assert books_list == ['1984', 'Мастер и Маргарита', 'Убить пересмешника', ]
