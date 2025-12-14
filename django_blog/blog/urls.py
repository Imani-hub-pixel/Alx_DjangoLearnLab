from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,CommentCreateView, CommentUpdateView,
    CommentDeleteView,PostSearchView, PostByTagListView,
    
    login_view, logout_view, register_view, profile_view, edit_profile_view,home_view,
)

urlpatterns = [

    #seacrh and tags
    path("search/", PostSearchView.as_view(), name="post_search"),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts_by_tag"),
    #comments urls
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment_create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),


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