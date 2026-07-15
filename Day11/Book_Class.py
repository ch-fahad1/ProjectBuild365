class Book:

    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book("Python", "John", 1500)

book1.display()