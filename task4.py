class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently borrowed.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have returned '{book.title}'.")
                    return
                else:
                    print(f"Book '{book.title}' was not borrowed.")
                    return
        print(f"Book '{title}' not found in the library.")

    def view_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books available at the moment.")

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add book")
            print("2. Borrow book")
            print("3. Return book")
            print("4. View available books")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                self.add_book(title, author)
            elif choice == '2':
                title = input("Enter book title: ")
                self.borrow_book(title)
            elif choice == '3':
                title = input("Enter book title: ")
                self.return_book(title)
            elif choice == '4':
                self.view_available_books()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

# Run the Library Management System
library = Library()
library.run()
