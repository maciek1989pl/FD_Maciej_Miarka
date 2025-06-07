from books import Book, books


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, author, title, year_of_release, pages, amount):
        if book_id in self.books:
            print("Książka już istnieje")
        else:
            new_book = Book(book_id, author, title, year_of_release, pages, amount)
            self.books[book_id] = new_book
            print(f"Dodano książkę {title}")

    def edit_book(self, book_id, author=None, title=None, year_of_release=None, pages=None, amount=None):
        if book_id in self.books:
            book = self.books[book_id]
            if author is not None:
                book.author = author
            if title is not None:
                book.title = title
            if year_of_release is not None:
                book.year_of_release = year_of_release
            if pages is not None:
                book.pages = pages
            if amount is not None:
                book.amount = amount
            print(f"Zaktualizowano książkę o ID {book_id}")
        else:
            print(f"Książka o ID {book_id} nie istnieje.")

    def delete_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Usunięto książkę: {removed.title} (ID: {book_id})")
        else:
            print(f"Książka o ID {book_id} nie istnieje.")