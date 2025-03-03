class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        
    def __str__(self):
        books = ', '.join(book.title for book in self.borrowed_books) or "No books borrowed"
        return f"Member: {self.name}, Borrowed Books: {books}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if book is None:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if member is None:
            raise ValueError(f"Member '{member_name}' not found.")
        
        member.borrow_book(book)
    
    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        
        if member is None:
            raise ValueError(f"Member '{member_name}' not found.")
        if book is None:
            raise BookNotFoundException(f"Book '{book_title}' is not borrowed by {member_name}.")
        
        member.return_book(book)
    
    def display_books(self):
        for book in self.books:
            print(book)
    
    def display_members(self):
        for member in self.members:
            print(member)

# Example usage
library = Library()

# Adding books
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

# Adding members
library.add_member(Member("Alice"))
library.add_member(Member("Bob"))

# Borrowing books
try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "Moby Dick")  # This should raise an exception
except Exception as e:
    print(e)

# Displaying current status
library.display_books()
library.display_members()

# Returning a book
try:
    library.return_book("Alice", "1984")
except Exception as e:
    print(e)

# Display final state
library.display_books()
library.display_members()