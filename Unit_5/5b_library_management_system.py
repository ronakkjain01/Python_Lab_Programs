print("LIBRARY MANAGEMENT SYSTEM")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        print("\nAVAILABLE BOOKS")
        if len(self.books) == 0:
            print("No books available")
        else:
            for book in self.books:
                print(book)

library = Library()
n = int(input("Enter the number of books: "))
for i in range(n):
    book = input("Enter book name: ")
    library.add_book(book)
library.display_books()
