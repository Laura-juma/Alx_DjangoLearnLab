from django.urls import path
from .views import list_books_view
from .views import LibraryDetailsView

urlpatterns = [
path('books/', list_books_view, name='books'),
path('library/<int:pk>/', LibraryDetailsView.as_view(), name='library_detail'), 
  
]
