# Создание функций для работы с библиотекой(загрузка и сохранени данных)
import json
from typing import List, Dict, Union

def load_data() -> List[Dict[str, Union[int, str]]]:
    try:
        with open('library.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(data: List[Dict[str, Union[int, str]]]) -> None:
    with open('library.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# Блок кода отвечающий за добавление книг
def add_book(title: str, author: str, year: int) -> None:
    data = load_data()
    new_book = {
        'id': len(data) + 1,
        'title': title,
        'author': author,
        'year': year,
        'status': 'в наличии'
    }
    data.append(new_book)
    save_data(data)
    print('Книга успешно добавлена.')

# Блок кода отвечающий за удаление
def delete_book(book_id: int) -> None:
    data = load_data()
    for book in data:
        if book['id'] == book_id:
            data.remove(book)
            save_data(data)
            print('Книга успешно удалена.')
            return
    print('Книга с таким ID не найдена.')

# Блок кода отвечающий поиск
def search_book(query: str) -> None:
    data = load_data()
    result = []
    for book in data:
        if query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query in str(book['year']):
            result.append(book)
    if result:
        print('Результаты поиска:')
        for book in result:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
    else:
        print('Книги по вашему запросу не найдены.')

# Блок кода отвечающий за вызов всего списка книг
def display_books() -> None:
    data = load_data()
    if not data:
        print('Список книг пуст.')
    else:
        print('Все книги в библиотеке:')
        for book in data:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")

# Блок кода отвечающий за изменение статуса
def change_status(book_id: int, new_status: str) -> None:
    data = load_data()
    for book in data:
        if book['id'] == book_id:
            book['status'] = new_status
            save_data(data)
            print('Статус книги успешно изменен.')
            return
    print('Книга с таким ID не найдена.')

# Блок кода отвечающий выполнение команд пользователя
def input_inf(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Ошибка ввода. Пожалуйста, введите значение.")

print('Для работы с приложением введите команду и нажмите "Enter"\n'
      '1. add - Позволяет добавить новую книгу \n'
      '2. delete - Позволяет удалить книгу \n'
      '3. search - Команда для поиска книги, достаточно ввести одно из (id, писатель, название книги)\n'
      '4. display - Выводит весь список книг\n'
      '5. change - Команда для изменения статуса книги\n'
      '6. exit - Завершение работы\n')

while True:
    command = input('Строка для ввода команды :')
    if command == 'add':
        title = input_inf('Введите название книги: ')
        author = input_inf('Введите автора книги: ')
        try:
            year = int(input_inf('Введите год издания: '))
            add_book(title, author, year)
        except ValueError:
            print("Ошибка: Год издания должен быть числом.")
    elif command == 'delete':
        try:
            book_id = int(input('Введите ID книги для удаления: '))
            delete_book(book_id)
        except ValueError:
            print("Ошибка: ID должен быть числом.")
    elif command == 'search':
        query = input('Введите запрос для поиска: ')
        search_book(query)
    elif command == 'display':
        display_books()
    elif command == 'change':
        try:
            book_id = int(input('Введите ID книги для изменения статуса: '))
            new_status = input('Введите новый статус книги: ')
            change_status(book_id, new_status)
        except ValueError:
            print("Ошибка: ID должен быть числом.")
    elif command == 'exit':
        break
    else:
        print("Возможно произошла опечатка?")