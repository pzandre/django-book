from django import forms
from .models import Book, Author

class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
