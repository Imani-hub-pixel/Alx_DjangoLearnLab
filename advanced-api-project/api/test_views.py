from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create a test book
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

   
    # Test List Books
   
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")

    
    # Test Retrieve Single Book
   
    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

  
    # Test Create Book - Authenticated
  
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-create')
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "No Longer at Ease")

   
    # Test Create Book - Unauthenticated
 
    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Unauth Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # permission denied

  
    # Test Update Book
 
    def test_update_book(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-update', kwargs={'pk': self.book.id})
        data = {
            "title": "Things Fall Apart - Updated",
            "publication_year": 1959
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Things Fall Apart - Updated")
        self.assertEqual(self.book.publication_year, 1959)

  
    # Test Delete Book
   
    def test_delete_book(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-delete', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

   
    # Test Search/Filter Books
   
    def test_search_books(self):
        url = reverse('book-list') + '?search=Things'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
