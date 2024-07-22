import json
from book import Book
from typing import Optional

class Library:
    """Описание библиотеки
    
    Attributes:
        books: Список в котором хранятся объкты Book,
        data_file: Путь к JSON файлу с данными
    """
    
    def __init__(self, data_file="data.json") -> None:
        """Подгружает данные из файла JSON при инициализации класса"""
        self.data_file = data_file
        self.load_data()


    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку

        Args:
            title: Название книги,
            author: Автор книги,
            year: Год издания книги
        """

        book = Book(title, author, year, data_file=self.data_file)
        self.books.append(book)

        self.save_data()
        print(f'{book} успешно добавлена.\n')
        

    def load_data(self) -> None: 
        """Загружает данные из JSON файла в список книг"""

        try:
            with open(self.data_file, 'r') as file:
                self.books = [Book(**kwargs) for kwargs in json.load(file)]
        except FileNotFoundError:
            self.books = []


    def save_data(self) -> None:
        """Записывает данные из списка книг в JSON файл"""

        with open(self.data_file, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file)

    
    def delete_book(self, id: int) -> None:
        """Удаляет книгу из списка книг по id

        Args:
            id: Уникальный идентификатор книги
        """

        book = self.search_book_by_id(id)
        
        if book:
            self.books.remove(book)
            self.save_data()
            print(f'Книга с ID {id} успешно удалена.\n')
        else:
            print(f'Книги с ID {id} не нашлось.\n')


    def search_book_by_id(self, id: int) -> Optional[Book]:
        """Находит книгу по уникальному идентификатору

        Args:
            id: Уникальный идентификатор книги

        Returns:
            Либо объект Book если нашлась книга с нужным id,
            либо None если не нашлось такой книги
        """

        result = None
        for book in self.books:
            if book.id == id:
                result = book
        
        return result


    def search_books_by_title(self, title: str) -> list[Book]:
        """Находит книги по названию

        Args:
            title: Название книги

        Returns:
            Список из объектов Book у которых название title, 
            либо пустой список если нет книг с таким названием

        """

        result = []

        for book in self.books:
            if book.title == title:
                result.append(book)

        return result


    def search_books_by_author(self, author: str) -> list[Book]:
        """Находит книги по автору

        Args:
            author: Автор книги

        Returns:
            Список из объектов Book, у которых автор author,
            либо пустой список если нет книг с таким автором
        """

        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
        
        return result
    
    
    def search_books_by_year(self, year: int) -> list[Book]:
        """Находит книги по году издания

        Args:
            year: Год издания

        Returns:
            Список из объектов Book, у которых год издания year,
            либо пустой список если нет книг с таким годом издания
        """

        result = []
        for book in self.books:
            if book.year == year:
                result.append(book)
        
        return result


    def show_all(self) -> None:
        """Отображает все книги из библиотеки"""

        count = len(self.books)
        print(f'Нашлось {count} книг:')
        for book in self.books:
            print(book)


    def change_status(self, id: int, status: str) -> None:
        """Меняет статус книги на заданный по уникальному идентификатору

        Args:
            id: Уникальный идентификатор книги
            status: Новый статус книги
        """

        book = self.search_book_by_id(id)
        if book:
            book.status = status 
            self.save_data()
            print(f'Статус книги с ID {id} успешно изменен.\n')
        else:
            print(f'Книги с id {id} не нашлось\n')
