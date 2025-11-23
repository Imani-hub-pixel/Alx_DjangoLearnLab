# bookshelf/forms.py
from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=100,
        strip=True,
        help_text="Search by title or author (max 100 chars)."
    )

    def clean_q(self):
        q = self.cleaned_data.get("q", "")
        return q
