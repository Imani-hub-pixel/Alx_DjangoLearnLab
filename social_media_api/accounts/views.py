from django.shortcuts import render
from .models import User
# Create your views here.
def register_view(request):
    return render(request, 'accounts/register.html')
def login_view(request):
    return render(request, 'accounts/login.html')

def profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'accounts/profile.html', {'user': user})
