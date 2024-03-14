class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:

    def __init__(self, books):
        self.books = books

    def take_book(self, title):
        to_remove = [b for b in self.books if b.title == title]
        self.books.remove(to_remove[0])
    