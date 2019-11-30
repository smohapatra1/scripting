#!/usr/bin/python
#Initialization of function
class person ():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print ("My name is " + self.name)

    def getAge(self):
        print ("My Age is " + self.age)
p = person ("samar", "34")
p.getName()
p.getAge()
