\# Retrieve Operation



\*\*Objective:\*\* Retrieve and display all attributes of the Book instance in the Django shell.



---



\*\*Command:\*\*



```python

from bookshelf.models import Book



\# Retrieve the book we just created

book = Book.objects.get(id=1)



\# Display the book

book  # <Book: Book object (1)>  <- expected output



