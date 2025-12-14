from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    login_view, logout_view, register_view, profile_view, edit_profile_view,home_view
)

urlpatterns = [


    path("", PostListView.as_view(), name="posts"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    path("",home_view, name="home"),
    path("login/",login_view, name="login"),
	path("logout/",logout_view, name="logout"),
    path("register/",register_view, name="register"),
    path("profile/",profile_view, name="profile"),
    path("profile/edit/",edit_profile_view, name="edit_profile"),
]