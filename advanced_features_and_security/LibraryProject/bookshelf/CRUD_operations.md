# CREATE Operation

**Command:**
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book

#Expected output
<Book: 1984>  

# RETRIEVE Operation

**Command:**
```python
from bookshelf.models import Book

# Retrieve and display all attributes of the created book
book = Book.objects.get(title="1984")
print(book.id, book.title, book.author, book.publication_year)

#Expected output
2 1984 George Orwell 1949

# UPDATE Operation

**Command:**
```python
from bookshelf.models import Book

# Update the title of "1984" to "Nineteen Eighty-Four"
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)

#Expected output

Nineteen Eighty-Four


# DELETE Operation

**Command:**
```python
from bookshelf.models import Book

# Delete the book and confirm deletion
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Try retrieving all books again
Book.objects.all()

#expected output
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>