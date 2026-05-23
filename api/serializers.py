from .models import Book, Author
from rest_framework import serializers
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
   
  def validate(self, data):
    if data['publication_year'] > timezone.now().year:
      raise serializers.ValidationError("Publication year cannot be in the Future")
    return data

  class Meta:
    model = Book
    fields = '__all__'
    

class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many = True)

  class Meta:
    model = Author
    fields = ['name', 'books']