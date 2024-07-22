import os
import sys
import json
from unittest import TestCase, main 

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from book import Book


class BookTest(TestCase):

    def setUp(self):
        self.test_data = "test_data.json"
        
        with open(self.test_data, "w") as file:
            json.dump([], file)


    def tearDown(self):
        os.remove(self.test_data)


    def test_create_id(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)
        id = book.id

        self.assertEqual(id, 1)


    def test_to_dict(self):
        book = Book("Name", "Author", 2024, data_file=self.test_data)

        self.assertEqual(book.to_dict(), {"id": 1, "title": "Name", "author": "Author", "year": 2024, "status": "в наличии"})

    

if __name__ == "__main__":
    main()
