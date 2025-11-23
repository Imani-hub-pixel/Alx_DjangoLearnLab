from django.shortcuts import render

# Create your views here.
from rest_framework import generics,viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

class BookViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD operations for Book model.
    Only authenticated users can access endpoints.
    Authentication method: TokenAuthentication
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



