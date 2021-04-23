from django.urls import path
from .views import HomeView, BookDetailView, UpdateBookView, AddBookView, DeleteBookView, BookSearchView, AddAuthorView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('add_book/', AddBookView.as_view(), name='add-book'),
    path('add_author/', AddAuthorView.as_view(), name='add-author'),
    path('book/edit/<int:pk>', UpdateBookView.as_view(), name='update-book'),
    path('book/<int:pk>/delete', DeleteBookView.as_view(), name='delete-book'),
    path('search/', BookSearchView.as_view(), name='search'),
]
