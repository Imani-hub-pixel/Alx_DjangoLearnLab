from django.shortcuts import render

# Create your views here.
from .models import Author, Book, Library, Librarian
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
def list_books(request):
    books=Book.objects.all()
    return render(request,"relationship_app/list_books.html",{"books":books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"