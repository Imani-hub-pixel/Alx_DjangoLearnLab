from .models import Author, Book, Library, Librarian


author_name = "John Doe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)

    print("Books written by {author_name}:")
    for book in books_by_author:
        print(f"{book.title}")
except Author.DoesNotExist:
    print(f"{author_name} not found.")

library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()

    print("Books available in {library_name}:")
    for book in books_in_library:
        print(f"{book.title}")
except Library.DoesNotExist:
    print(f"{library_name} not found.")


try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"{library_name} not found.")
except Librarian.DoesNotExist:
    print(f"No librarian found for {library_name}.")

