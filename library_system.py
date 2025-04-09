class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies=1):
        if copies <= 0:
            raise ValueError("Number of copies must be positive.")
        if title in self.books:
            self.books[title] += copies
        else:
            self.books[title] = copies

    def borrow_book(self, title):
        if title not in self.books or self.books[title] == 0:
            raise ValueError("Book not available.")
        self.books[title] -= 1

    def return_book(self, title):
        if title not in self.books:
            self.books[title] = 1
        else:
            self.books[title] += 1

    def get_copies(self, title):
        return self.books.get(title, 0)
