#!/usr/bin/python
#Initialize a function 
class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def getName(self):
        print ("My Name is " +  self.name)
    def getAge(self):
        print ("My Age is " + self.age)
p = person("Samar", "34")
p.getName()
p.getAge()
