from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # assuming you have a ModelForm for Book

# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import Book
from .forms import BookSearchForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def book_list(request):
    """
    Safe search handling using Django ORM and validated input.
    Avoid building SQL strings with string formatting.
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        q = form.cleaned_data.get("q", "")
        if q:
            # Use ORM filters (parameterized safely)
            # Example: search title or author (case-insensitive)
            books = Book.objects.filter(
                title__icontains=q
            ) | Book.objects.filter(author__icontains=q)
        else:
            books = Book.objects.all()[:200]  # limit results
    else:
        # if invalid, return no results or handle gracefully
        books = Book.objects.all()[:50]

    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})


@require_http_methods(["POST"])
def submit_form(request):
    """
    Example of using Django forms and CSRF protection for POST.
    """
    # Suppose you have a form class for submission; this is a placeholder.
    # The template includes {% csrf_token %} and Django's CsrfViewMiddleware enforces tokens.
    # Do not use raw SQL with string formatting. If you must use raw SQL, always use parameters.
    # Example of safe raw SQL with parameters:
    q = request.POST.get("q", "").strip()
    if q:
        with connection.cursor() as cursor:
            # Use param placeholders to avoid injection (db backend will parameterize)
            cursor.execute("SELECT id, title FROM bookshelf_book WHERE title LIKE %s", [f"%{q}%"])
            rows = cursor.fetchall()
            # transform rows to objects or context as needed (prefer ORM)
            
    return redirect("bookshelf:book_list")


# View a book (requires can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

# Create a book (requires can_create)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

# Edit a book (requires can_edit)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

# Delete a book (requires can_delete)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

"""
Permissions Setup:

Book model has custom permissions:
- can_view: Allows viewing book details
- can_create: Allows creating new books
- can_edit: Allows editing books
- can_delete: Allows deleting books

Groups:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Usage:
- @permission_required('bookshelf.can_edit', raise_exception=True) protects edit views
- Users must be assigned to appropriate group to access features
"""
