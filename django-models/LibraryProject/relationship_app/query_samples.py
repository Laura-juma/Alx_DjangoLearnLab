from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name ="Jon Snow")
books_by_author = author.books.all

library = Library.objects.get(name="library_name")
books_in_library = library.books.all()

for book in books_in_library:
  print(book.title)


library = Library.objects.get(name="library_name")
library.librarian

