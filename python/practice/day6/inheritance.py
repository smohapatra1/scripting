#!/usr/bin/python
#Function/Class Inheritance
class parent():
    def __init__(self):
        print ("This is a parent class")
    def parentFunc(self):
        print ("This is a parent Func")
p=parent()
p.parentFunc()
class child(parent):
    def __init__(self):
        print("This is a child class")
    def childFunc(self):
        print ("This is a child func")
c=child()
c.childFunc()
class child(parent):
    def __self__(self):
        pass
    def test(self):
        print ("parent")
d = child()
d.test()
class child(parent):
    def __self__(self):
        pass
    def test(self):
        print ("child")
e= child()
e.test()
