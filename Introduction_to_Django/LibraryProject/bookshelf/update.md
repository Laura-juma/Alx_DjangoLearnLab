\# Update Operation



\*\*Objective:\*\* Update the title of the Book instance in the Django shell.



---



\*\*Command:\*\*



```python

from bookshelf.models import Book



\\# Retrieve the book we want to update

book = Book.objects.get(id=1)



\\# Update the title

book.title = "Nineteen Eighty-Four"

book.save()  # Save the change to the database



\\# Verify the update

book = Book.objects.get(id=1)

book  # <Book: Book object (1)>  <- expected output

book.title  # 'Nineteen Eighty-Four'  <- expected output




