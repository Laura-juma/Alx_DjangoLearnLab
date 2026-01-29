\# Create Operation



\*\*Objective:\*\* Create a Book instance in the Django shell.



---



\*\*Command:\*\*



```python

from bookshelf.models import Book



\# Create a new book instance using objects.create

Book.objects.create(

&nbsp;   title="1984",

&nbsp;   author="George Orwell",

&nbsp;   publication\_year=1949

)  # <Book: Book object (1)>  <- expected output



