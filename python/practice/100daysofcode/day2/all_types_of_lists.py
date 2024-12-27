#!/usr/bin/python
x = [ "a" , "b", "c"]
#Prints ths lists
print ("prints all" , x)
#Prints the first list
print ("prints first", x[0])
#Prints appended data
x.append("d")
print ("appends d ", x)
x.reverse()
print ("reverse", x )
x.sort()
print ("sort", x)
x.insert(1, x[0])
print ("insert first list in 2nd place", x)
del (x[1])
print ("delete 2nd list", x)
x.pop()
print ("pops ", x)
x.pop(2)
print ("pops 2nd ", x)
x.remove("a")
print ("removes", x)
x.clear()
print ("Cleared", x)
