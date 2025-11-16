from django.urls import path
from .views import list_books, LibraryDetailView
from .views import CustomLoginView,CustomLogoutView, registration_view,home_view


urlpatterns = [
    path("",home_view,name='home'),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/",CustomLogoutView.as_view(), name="logout"),
    path("register/", registration_view, name="register"),

]

