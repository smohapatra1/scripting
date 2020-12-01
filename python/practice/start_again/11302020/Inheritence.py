#OOP - Inheritence 
class Animal():
    def __init__(self):
        print ("Animal Created! ")
    def who_am_i(self):
        print ("I am an animal")
    def eat(self):
        print ( " Animal is eating ")
class Dog(Animal):
   def __init__(self):
       Animal.__init__(self)
       print ("Dog Created")
       def eat(self):
           print ("Dog is eating!")
mydog = Dog()
mydog.eat()
mydog.who_am_i()