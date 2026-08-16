import library_utils as lib

try:
    lib.add_book("The Hobbit", "J.R.R. Tolkien", "9780618260300", "Fantasy")
    lib.add_book("Dune", "Frank Herbert", "9780441013593", "Sci-Fi")
    lib.add_book("1984", "George Orwell", "9780451524935", "Dystopian")
    lib.add_book("Brave New World", "Aldous Huxley", "9780060850524", "Dystopian")
except (lib.InvalidISBNError, lib.DuplicateBookError) as e:
    print(f"Error adding book: {e}")

# Invalid ISBN test
try:
    lib.add_book("Bad Book", "Unknown", "123", "Fiction")
except lib.InvalidISBNError as e:
    print(f"Error: {e}")

# Duplicate ISBN test
try:
    lib.add_book("Duplicate Hobbit", "Tolkien", "9780618260300", "Fantasy")
except lib.DuplicateBookError as e:
    print(f"Error: {e}")


try:
    print("\nFound:", lib.find_book("9780441013593"))
    lib.find_book("0000000000000")   # doesn't exist
except lib.BookNotFoundError as e:
    print(f"Error: {e}")


try:
    lib.update_book("9780441013593", genre="Science Fiction")
    print("After update:", lib.find_book("9780441013593"))
except lib.BookNotFoundError as e:
    print(f"Error: {e}")


mag = lib.Magazine("National Geographic", 245, "March 2026")
items = [lib.Book("Dune", "Frank Herbert", "9780441013593", "Sci-Fi"), mag]
print("\nAll items (polymorphism):")
for item in items:
    print(item.display_info())


print("\nUnique authors:", lib.unique_authors())
print("ISBN to title map:", lib.isbn_to_title_map())


print("\nBooks grouped by genre:", lib.books_by_genre())

print("\nSuggested reading pairs:")
for pair in lib.suggest_reading_pairs():
    print(pair)


print("\nSearch by author 'orwell':")
for r in lib.search_by_author("orwell"):
    print(r)


lib.export_to_csv()

try:
    lib.delete_book("9780618260300")
except lib.BookNotFoundError as e:
    print(f"Error: {e}")