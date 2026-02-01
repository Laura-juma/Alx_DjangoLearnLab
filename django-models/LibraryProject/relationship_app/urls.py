from django.urls import path
from .views import list_books_view
from .views import LibraryDetailView

urlpatterns = [
path('books/', list_books_view, name='books'),
path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
  
]
