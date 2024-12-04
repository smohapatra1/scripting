#   https://www.geeksforgeeks.org/why-do-python-classes-inherit-object/

class Name():
    pass
exp = Name()
print (isinstance(exp, object))

class Book():
    def __init__(self,title):
        self.title = title
    def __str__(self):
        return "Book: " + self.title
book = Book("Learn Python")
print (book)