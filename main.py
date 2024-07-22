from library import Library

def main() -> None:
    """Отображает меню действий и запрашивает действие у пользователя,
    затем производит это действие в библиотеке и сохраняет изменения
    """

    library = Library()
    correct_status = ('в наличии', 'выдана')
    
    while True:
        print('Меню действий:')
        print('1. Добавить новую книгу')
        print('2. Удалить книгу')
        print('3. Найти книги')
        print('4. Показать все книги')
        print('5. Изменить статус книги')
        print('6. Выйти')
        print()

        choice = input('Введите пункт меню: ')

        print()
        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            year = input('Введите год издания книги: ')

            if not year.isdigit():
                print('Год должен быть числом!\n')
                continue

            year = int(year)

            library.add_book(title, author, year)

        elif choice == '2':
            id = input('Введите id книги: ')
            
            if not id.isdigit():
                print('ID должен быть числом!\n')
                continue 
            id = int(id)
                
            library.delete_book(id)
        
        elif choice == '3':
            print('Выберите тип поиска:')
            print('1. Поиск по ID')
            print('2. Поиск по названию книги')
            print('3. Поиск по автору книги')
            print('4. Поиск по году издания')
            print()
            
            choice = input('Введите ваш выбор: ')

            if choice == '1':
                id = input('Введите id книги: ')

                if not id.isdigit():
                    print('ID должно быть числом!\n')
                    continue 
                id = int(id)
                print()
                
                book = library.search_book_by_id(id)
                if book:
                    print(book)
                    print()
                else:
                    print(f'Книги с ID {id} не нашлось.\n')
            elif choice == '2':
                title = input('Введите название книги: ')
                print()

                books = library.search_books_by_title(title)

                if books:
                    print(f'Найдено {len(books)} книг:')
                    for book in books:
                        print(book)
                    print()
                else:
                    print(f'Книг с названием {title} не нашлось\n')
            elif choice == '3':
                author = input('Введите автора книги: ')
                print()

                books = library.search_books_by_author(author)

                if books:
                    print(f'Найдено {len(books)} книг:')
                    for book in books:
                        print(book)
                    print()
                else:
                    print(f'Книг с автором {author} не нашлось\n')
            elif choice == '4':
                year = input('Введите год издания книги: ')

                if not year.isdigit():
                    print('Год должен быть числом!\n')
                    continue
                print()

                year = int(year)

                books = library.search_books_by_year(year)

                if books:
                    print(f'Найдено {len(books)} книг:')
                    for book in books:
                        print(book)
                    print()
                else:
                    print(f'Книг с годом издания {year} не нашлось\n')

            else:
                print('Неккоректный ввод!\n')
        elif choice == '4':
            library.show_all()
            print()
        elif choice == '5':
            id = input('Введите ID книги: ')
            if not id.isdigit():
                print('ID должно быть числом!\n')
                continue
            id = int(id)
            status = input('Введите новый статус книги: ')
            if status not in correct_status:
                print('Неккоректный статус!\n')
                continue           
            library.change_status(id, status)

        elif choice == '6':
            break
        else:
            print('Неккоректный ввод!\n')


if __name__ == "__main__":
    main()
