from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
      model = Book
      exclude = ["created_at", "updated_at"]
      widgets = {
            'pubdate': forms.DateInput(attrs={'type': 'date'})
      }