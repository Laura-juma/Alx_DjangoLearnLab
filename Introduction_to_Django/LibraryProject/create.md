from bookshelf.models import Book



my\_book= Book(

title="1984",

author= "George Orwell",

publication\_year= 1949

)



my\_book.save()  # Object is saved



Book.objects.all()  # <QuerySet \[<Book: 1984>]>  <- expected output

