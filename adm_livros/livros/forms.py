from django import forms
from .models import Book

class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'