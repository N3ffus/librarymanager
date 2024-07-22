import json
from typing import Optional
class Book:
    """Описание книги

    Attributes:
        id: Уникальный идентификатор книги
        title: Название книги
        author: Автор книги
        year: Год издания книги
        status: Статус книги, один из видов: "выдана" или "в наличии"
        data_file: Путь к JSON файлу с данными
    """

    def __init__(self, title: str, author: str, year: int, id: Optional[int] = None, status: str = 'в наличии', data_file="data.json"):
        """Инициализирует аргументы книги"""
        
        self.title = title 
        self.author = author
        self.year = year 
        self.status = status
        self.data_file = data_file
        if id is None:
            self.id = self.create_id()
        else:
            self.id = id 

    
    def to_dict(self) -> dict:
        """Преобразует класс книги в тип словаря

        Returns:
            Словарь с ключами, являющимися аргументами книги:
            id, title, author, year, status
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }


    def create_id(self) -> int:
        """Создает уникальный id каждой книги

        Returns:
            Число которое является уникальным id книги
        """
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                mx = 0
                for book in data:
                    mx = max(mx, book["id"])
                return mx+1
        except FileNotFoundError:
            return 1
        

    def __repr__(self) -> str:
        return f'Книга "{self.title}", автор: {self.author}, год издания: {self.year}, статус: {self.status}, ID: {self.id}'
