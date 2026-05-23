from django.contrib import admin


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Author, Book, Library, Librarian

class CustomUserAdmin(UserAdmin):
    model = UserProfile

  
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

    
    list_filter = ('role', 'is_staff', 'is_active')

    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(UserProfile, CustomUserAdmin)


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
