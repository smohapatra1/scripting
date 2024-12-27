#!/usr/bin/python
#Set
x = { "a", "b", "c" }
print ("Get vars", x)
#Remove
x.remove("a")
print ("Removed a ", x)
#Add
x.add("a")
print ("Added a ", x)
#Update
y = {"d", "e", "f"}
x.update(y)
print ("Update", x)
#Discard
x.discard("d")
x.discard("e")
x.discard("f")
print ("Discarded new values", x)
#POP doesnot take any arguments
x.pop()
print ("Poped", x)
#Clear
x.clear()
print ("Cleared", x)
x = {"a", "b" , "c"}
#Constructor
y = set(("x", "y", "z"))
print ("Set constructor", y)
#Delete
del x
print ("Delete - Will raise an error", x)

