from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as df_filters

class BookFilter(df_filters.FilterSet):
    title = df_filters.CharFilter(lookup_expr= 'icontains')
    authorname = df_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
       
    class Meta:
       model = Book
       fields = ['title', 'authorname', 'publication_year']

class BookListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_class = BookFilter
  search_fields = ['title', 'author__name']
  ordering_fields = ['title', 'publication_year']
  




class BookCreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    print(f"Book created by: {self.request.user.username}")

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


