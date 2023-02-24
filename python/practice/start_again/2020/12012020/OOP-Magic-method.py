#Magic method
class books ():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages 
        print (f"{self.name} by {self.author} having {self.pages} pages")      
    def __str__(self):
        return (f"{self.name} by {self.author}")
b = books("Python Rocks !", "Samar", "300")
print (b)