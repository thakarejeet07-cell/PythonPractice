import os,json,re,csv
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
    with open(FILENAME,"w") as file:
        json.dump(books, file, indent=4)    


def export_to_csv(csv_filename = "library.csv"):
    books = load_books()
    with open(csv_filename,"w",newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "isbn", "genre"])
        writer.writeheader()
        writer.writerows(books)
    print(f"Exported to {csv_filename}")

def add_book(title, author, isbn, genre):
    validate_isbn(isbn)
    books = load_books()

    if any(b["isbn"] == isbn for b in books):
        raise DuplicateBookError(f"Book with ISBN {isbn} already exists")
    
    book = Book(title, author, isbn, genre)
    books.append(book.to_dict())

    save_books(books)
    print(f"Added: {book.display_info()}")


def find_book(isbn):
    books = load_books()
    for b in books:
        if b["isbn"] == isbn:
            return b
    raise BookNotFoundError(f"No book found with ISBN {isbn}")


def update_book(isbn, **kwargs):
    books = load_books()
    for b in books:
        if b["isbn"] == isbn:
            for key,value in kwargs.items():
                if key in b:
                    b[key] = value
                else:
                    print(f"Warning: '{key}' is not a valid field, skipped")
            save_books(books)
            print(f"Updated book {isbn}: {kwargs}")
            return
    raise BookNotFoundError(f"No book found with ISBN {isbn}")   
    


def delete_book(isbn):
    books = load_books()
    updated = [b for b in books if b["isbn"] != isbn]
    if len(updated) == len(books):
        raise BookNotFoundError(f"No book found with ISBN {isbn}")    
    save_books(updated)
    print(f"Deleted book with ISBN {isbn}")

def unique_authors():
    books = load_books()
    return {b["author"] for b in books}  


def isbn_to_title_map():
    books = load_books()
    return {b["isbn"] : b["title"] for b in books}

def books_by_genre():
    books = load_books()
    books.sort(key=lambda b: b["genre"])
    grouped = {}
    for genre,group in groupby(books, key=lambda b: b["genre"]):
        grouped[genre] = [b["title"] for b in group] 
    return grouped

def suggest_reading_pairs():
    books = load_books()
    titles = [b["title"] for b in books]
    return list(combinations(titles, 2))




            

              

