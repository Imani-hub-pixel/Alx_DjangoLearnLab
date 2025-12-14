from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CommentForm, RegisterForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.shortcuts import render

def home_view(request):
    return render(request, "blog/home.html")


def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration successful")
            return redirect("profile")
    else:
        form=RegisterForm()
    return render(request,"blog/register.html",{"form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()

    return render(request, "blog/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile_view(request):
    return render(request, "blog/profile.html")

@login_required
def edit_profile_view(request):
    user = request.user

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()
        messages.success(request, "Profile updated successfully")
        return redirect("profile")

    return render(request, "blog/edit_profile.html", {"user": user})

class PostListView(ListView):
    model=Post
    template_name="blog/post_list.html"
    context_object_name="posts"
    ordering=["-published_date"]
    paginate_by=5

class PostDetailView(DetailView):
    model=Post
    template_name="blog/post_detail.html"
    context_object_name="post"

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name="blog/post_form.html"
    fields=["title","content"]

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request, "Post created successfully")
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name="blog/post_form.html"
    fields=["title","content"]

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request, "Post updated successfully")
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
@login_required
def add_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully")
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "You are not allowed to edit this comment.")
        return redirect("post_detail", pk=comment.post.pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect("post_detail", pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/comment_form.html", {"form": form, "post": comment.post})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "You are not allowed to delete this comment.")
        return redirect("post_detail", pk=comment.post.pk)

    if request.method == "POST":
        post_pk = comment.post.pk
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect("post_detail", pk=post_pk)

    return render(request, "blog/comment_confirm_delete.html", {"comment": comment})

