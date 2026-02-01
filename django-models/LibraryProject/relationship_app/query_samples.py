from relationship_app.models import Author, Book, Library, Librarian


author_name = "John Doe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)


library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

for book in books_in_library:
    print(book.titlle)


library_name = "Central Library"
library = Library.objects.get(name=library_name)
librarian_qs = Librarian.objects.filter(library=library)
librarian = librarian_qs.first()

print(librarian.name)