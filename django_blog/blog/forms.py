from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  get_user_model
from .models import Comment,Post
from taggit.forms import TagWidget

User=get_user_model()

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Comment here..."
        }),
        max_length=1000,
        required=True
    )

    class Meta:
        model = Comment  
        fields = ["content"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5}),
            "tags":TagWidget(),
        }
    
        
