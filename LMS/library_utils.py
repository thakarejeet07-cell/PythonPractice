import os,json,re
from abc import ABC, abstractmethod
from itertools import groupby, combinations

class BookNotFoundError(Exception):
    pass

class InvalidISBNError(Exception):
    pass

class DuplicateBookError(Exception):
    pass

class LibraryItem(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre

    def display_info(self):
        return f"{self.title} by {self.author} [{self.genre}] - ISBN: {self.isbn}"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "genre": self.genre}

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, month):
        self.title = title
        self.issue_number = issue_number
        self.month = month

    def display_info(self):
        return f"{self.title} - Issue #{self.issue_number} ({self.month})"



FILENAME = "library.json"


def validate_isbn(isbn):  
    if not re.fullmatch(r"\d{13}", isbn):
        raise InvalidISBNError(f"'{isbn}' is not a valid 13-digit ISBN")
    return True

def search_by_author(name):
    books = load_books()
    pattern = re.compile(re.escape(name), re.IGNORECASE)
    return [b for b in books if pattern.search(b["author"])]

def load_books():
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME,"r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Library file corrupted, starting fresh.")
        return []

def save_books(books):
    with open("FILENAME","w") as file:
        json.dump(books, file, indent=4)      

