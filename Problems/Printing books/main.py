class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    # define the necessary method here
    def __str__(self):
        return f"{self.title} by {self.author}. ${self.price}. [{self.book_id}]"

#
# new_book = Book("George Orwell", "1984", 13.59, 1956789)
# print(new_book)