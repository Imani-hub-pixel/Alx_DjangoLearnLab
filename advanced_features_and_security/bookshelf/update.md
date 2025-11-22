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