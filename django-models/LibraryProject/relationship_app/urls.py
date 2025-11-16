from django.urls import path
from .views import list_books, LibraryDetailView
from .views import CustomLoginView,CustomLogoutView,home_view
from .views import register
from . import views


urlpatterns = [
    path("",home_view,name='home'),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", CustomLoginView.as_view(template_name="login.html"), name="login"),
    path("logout/",CustomLogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", views.register, name="register"),

]

