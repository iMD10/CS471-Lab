from django import forms
from .models import Book ,Student, Library

class BookForm(forms.ModelForm):
    class Meta:
      model = Book
      exclude = ["created_at", "updated_at"]
      widgets = {
            'pubdate': forms.DateInput(attrs={'type': 'date'})
      }

class StudentForm(forms.ModelForm):
   class Meta:
      model = Student
      fields = "__all__"

class LibraryForm(forms.ModelForm):
   class Meta:
      model = Library
      fields = "__all__"
   def show_image(self):
      if self.instance and self.instance.image:
          return f'<img src="{self.instance.image.url}" width="150" />'
      return ""