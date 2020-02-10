#Exercise Question 2: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
import os
def add_remove(x):
    print("Removing index 4 = from " , x )
    y = x.pop(4)
    print (y)
    print ("Inserting index 4 in 2nd place from " , x)
    z = x.insert(2, y)
    print (z)
#    a = x.append(y)
#    print (a)
add_remove([10, 11, 12, 13, 14, 15])
