# Retrieve Operation

**Objective:** Retrieve and display all attributes of the Book instance in the Django shell.

---

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book by its title
book = Book.objects.get(title="1984")

# Display the book
book  # <Book: Book object (1)>  <- expected output

# Display individual attributes
book.title            # '1984'
book.author           # 'George Orwell'
book.publication_year # 1949




