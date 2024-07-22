import os
import sys
import json
from unittest import TestCase, main

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from library import Library
from book import Book


class LibraryTest(TestCase):

    def setUp(self):
        self.test_data = "test_data.json"

        with open(self.test_data, "w") as file:
            json.dump([], file)

        self.library = Library(data_file=self.test_data)
    

    def tearDown(self):
        os.remove(self.test_data)


    def test_add_book(self):
        self.library.add_book("Name", "Author", 2024)

        self.assertEqual(len(self.library.books), 1)

    
    def test_load_data(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        
        with open(self.test_data, "w") as file:
            json.dump([book.to_dict()], file)


        self.library.load_data()

        self.assertEqual(self.library.books[0].id, 1)
        self.assertEqual(self.library.books[0].title, "Name")
        self.assertEqual(self.library.books[0].author, "Author")
        self.assertEqual(self.library.books[0].year, 2024)
        self.assertEqual(self.library.books[0].status, "в наличии")

    
    def test_save_data(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        self.library.books.append(book)

        self.library.save_data()
        self.library.load_data()

        self.assertEqual(book.id, self.library.books[0].id)
        self.assertEqual(book.title, self.library.books[0].title)
        self.assertEqual(book.author, self.library.books[0].author)
        self.assertEqual(book.year, self.library.books[0].year)
        self.assertEqual(book.status, self.library.books[0].status)


    def test_delete_book(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        self.library.books.append(book)

        self.library.delete_book(2)
        self.assertEqual(len(self.library.books), 1)
        self.library.delete_book(1)
        self.assertEqual(len(self.library.books), 0)

    
    def test_search_book_by_id(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        self.library.books.append(book)

        self.assertEqual(self.library.search_book_by_id(1), book) 
        self.assertIsNone(self.library.search_book_by_id(2))

    
    def test_search_book_by_title(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        self.library.books.append(book)
        book1 = Book("Name1", "Author1", 2023, data_file=self.test_data)
        self.library.books.append(book1)
        book2 = Book("Name1", "Author2", 2022, data_file=self.test_data)
        self.library.books.append(book2)

        self.assertEqual(self.library.search_books_by_title("Name2"), [])
        self.assertEqual(self.library.search_books_by_title("Name"), [book])
        self.assertEqual(self.library.search_books_by_title("Name1"), [book1, book2])

    
    def test_search_book_by_author(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        self.library.books.append(book)
        book1 = Book("Name1", "Author1", 2023, data_file=self.test_data)
        self.library.books.append(book1)
        book2 = Book("Name1", "Author1", 2022, data_file=self.test_data)
        self.library.books.append(book2)


        self.assertEqual(self.library.search_books_by_author("Author"), [book])
        self.assertEqual(self.library.search_books_by_author("Author2"), [])
        self.assertEqual(self.library.search_books_by_author("Author1"), [book1, book2])

    
    def test_search_book_by_year(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        self.library.books.append(book)
        book1 = Book("Name1", "Author1", 2024, data_file=self.test_data)
        self.library.books.append(book1)
        book2 = Book("Name1", "Author1", 2023, data_file=self.test_data)
        self.library.books.append(book2)


        self.assertEqual(self.library.search_books_by_year(2024), [book, book1])
        self.assertEqual(self.library.search_books_by_year(2023), [book2])
        self.assertEqual(self.library.search_books_by_year(2022), [])


    def test_change_status(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        self.library.books.append(book)

        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

        self.library.change_status(1, "в наличии")
        self.assertEqual(self.library.books[0].status, "в наличии")
    

if __name__ == "__main__":
    main()
