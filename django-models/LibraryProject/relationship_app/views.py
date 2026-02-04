from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from .models import UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

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



def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
      form = UserCreationForm()

  return render(request, 'relationship_app/register.html', {'form': form})


from django.contrib.auth import login
from django.contrib.auth import authenticate

"""def my_login_view(request):
  user = authenticate(username = "user", password="password")
  if user:
    login(request, user)"""

@login_required
def admin_view(request):
  if UserProfile.role != 'ADM':
    return redirect('no_access')
  
  context = {
    'message': 'Welcome to the admin page.'
  }

  return render(request, 'relationship_app/admin_view.html', context)


@login_required
def admin_view(request):
  if request.user.userprofile.role != 'LIB':
    return redirect('no_access')
  
  context = {
    'message': 'Welcome to the Librarian page.'
  }

  return render(request, 'relationship_app/admin_view.html', context)

@login_required
def librarian_view(request):
  if request.user.userprofile.role != 'LIB':
    return redirect('no_access')
  
  context = {
    'message': 'Welcome to the Librarian page.'
  }

  return render(request, 'relationship_app/librarian_view.html', context)

@login_required
def member_view(request):
  if request.user.userprofile.role != 'MEM':
    return redirect('no_access')
  
  context = {
    'message': "Welcome to the Member's page."
  }

  return render(request, 'relationship_app/member_view.html', context)




    
    







  
  










