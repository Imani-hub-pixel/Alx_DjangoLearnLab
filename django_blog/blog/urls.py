from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    login_view, logout_view, register_view, profile_view, edit_profile_view,home_view
)

urlpatterns = [


    path("", PostListView.as_view(), name="posts"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    path("",home_view, name="home"),
    path("login/",login_view, name="login"),
	path("logout/",logout_view, name="logout"),
    path("register/",register_view, name="register"),
    path("profile/",profile_view, name="profile"),
    path("profile/edit/",edit_profile_view, name="edit_profile"),
]