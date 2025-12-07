from django.shortcuts import render
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book,Author
from .serializers import BookSerializer
from django_filters import rest_framework as filters

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'author', 'publication_year']

    search_fields = ['title', 'author__name']

    ordering_fields = ['title', 'publication_year', 'author']
    ordering = ['title']
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]