from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from .models import UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

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

def is_admin(user):
    return user.userprofile.role == 'ADM'

def is_librarian(user):
    return user.userprofile.role == 'LIB'

def is_member(user):
    return user.userprofile.role == 'MEM'


@login_required
@user_passes_test(is_admin, login_url='no_access')
def admin_view(request):
    context = {
        'message': 'Welcome to the admin page.'
    }
    return render(request, 'relationship_app/admin_view.html', context)


@login_required
@user_passes_test(is_librarian, login_url='no_access')
def librarian_view(request):
    context = {
        'message': 'Welcome to the Librarian page.'
    }
    return render(request, 'relationship_app/librarian_view.html', context)


@login_required
@user_passes_test(is_member, login_url='no_access')
def member_view(request):
    context = {
        'message': "Welcome to the Member's page."
    }
    return render(request, 'relationship_app/member_view.html', context)

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        if author_id:
            book.author_id = author_id
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})






    
    







  
  










