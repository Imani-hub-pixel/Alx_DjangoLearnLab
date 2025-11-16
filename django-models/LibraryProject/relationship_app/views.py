from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

# Create your views here.
from .models import  Book
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from .models import Library

def list_books(request):
    books=Book.objects.all()
    return render(request,"relationship_app/list_books.html",{"books":books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'relationship_app/home.html')


class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Only save if valid
            user = form.save()
            # Log in the user automatically
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')  # redirect to a homepage/dashboard
        else:
            # Form is invalid, errors will be displayed in template
            return render(request, 'relationship_app/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})