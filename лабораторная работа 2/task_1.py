class Book:
    def __init__(self, id_: int, name: str, pages: int):
        # Сохраняем атрибуты. Важно использовать id_, как в шаблоне
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        # Для вывода: Книга "test_name_1"
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        # Для вывода в списке: Book(id_=1, name='test_name_1', pages=200)
        # !r автоматически добавит одинарные кавычки для имени
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # Выведет: Книга "test_name_1" и т.д.

    print(list_books)  # Выведет список объектов через __repr__
