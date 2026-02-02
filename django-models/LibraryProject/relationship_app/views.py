from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView


# Create your views here.
def list_books_view(request):
  books =Book.objects.all()
  
  context = {
    "books" : books
  }

  return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class register(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'relationship_app/register.html'

from django.contrib.auth import login
from django.contrib.auth import authenticate

"""def my_login_view(request):
  user = authenticate(username = "user", password="password")
  if user:
    login(request, user)"""



  
  










