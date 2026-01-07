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
from django.db.models import Q
from django.http import Http404
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

    def get_queryset(self):
        queryset = Post.objects.all()

        category = self.request.GET.get("category")
        author = self.request.GET.get("author")

        if category:
            queryset = queryset.filter(category__name__iexact=category)

        if author:
            queryset = queryset.filter(author__username__iexact=author)

        return queryset

    def get_ordering(self):
        ordering = self.request.GET.get("ordering")
        return ordering if ordering else "-published_date"

class PostDetailView(DetailView):
    model=Post
    template_name="blog/post_detail.html"
    context_object_name="post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  
        return context

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

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

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
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})
class PostSearchView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()



class PostByTagListView(ListView):
    model = Post
    template_name = "blog/posts_by_tag.html"  # template to render
    context_object_name = "posts"

    def get_queryset(self):
        tag_name = self.kwargs.get("tag_name")
        return Post.objects.filter(tags__name=tag_name).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_name"] = self.kwargs.get("tag_name")
        return context


def get_queryset(self):
    queryset = Post.objects.all()

    category = self.request.GET.get("category")
    if category and not queryset.filter(category__name__iexact=category).exists():
        raise Http404("Category not found")

    return queryset
