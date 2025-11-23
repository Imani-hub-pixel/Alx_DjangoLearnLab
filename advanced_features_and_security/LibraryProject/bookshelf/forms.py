# bookshelf/forms.py
from django import forms

# Form used in form_example.html
class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter your name"
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
        help_text="Enter your message"
    )


# Search form for book_list.html
class BookSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=100,
        strip=True,
        help_text="Search by title or author (max 100 chars)"
    )
