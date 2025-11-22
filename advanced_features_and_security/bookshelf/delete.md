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