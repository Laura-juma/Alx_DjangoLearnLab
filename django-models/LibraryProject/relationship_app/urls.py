from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import admin_view, librarian_view, member_view



urlpatterns = [
    
    path('books/', views.list_books_view, name='books'),

    
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),

    
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),

    
    path(
        'register/',
        views.register,
        name='register'
    ),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]  



