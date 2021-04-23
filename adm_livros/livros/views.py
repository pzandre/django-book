from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q 

from .models import Book
from .forms import BookAddForm, UpdateBookForm

class HomeView(ListView):
    model = Book
    template_name = 'home.html'


class AddBookView(CreateView):
    model = Book
    template_name = 'add_book.html'
    form_class = BookAddForm
    success_url = reverse_lazy('home')


class UpdateBookView(UpdateView):
    model = Book
    form_class = UpdateBookForm
    template_name = 'update_book.html'
    success_url = reverse_lazy('home')


class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('home')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'


class BookSearchView(ListView):
    models = Book
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Book.objects.filter(Q(name__icontains=query))
        else:
            object_list = None
        return object_list
