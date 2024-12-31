#   https://www.geeksforgeeks.org/python-library-for-linked-list/

import structlinks 
from structlinks import LinkedList 

# create an empty linked list 
lst = LinkedList() 

# create a linked list with initial values 
lst = LinkedList([1, 10.0, 'string']) 

print(lst) 

print() 

print('Elements of list:') 

# elements of the list 
element0 = lst[0] 
element1 = lst[1] 
element2 = lst[2] 

print(f'first element : {element0}') 
print(f'second element : {element1 }') 
print(f'third element : {element2}') 

print() 

print('Length of list:') 

# Length of the list 
length = len(lst) 

print(f'size of the list : {length}') 

print() 

print('Set item:') 

# Set item 
lst[0] = 10

print(f'list after setting lst[0] to 10 : {lst}') 

print() 

print('Append And Insert:') 

# Append And Insert 
lst.append('another string') 
lst.insert(1, 0.0) 

print(f'list after appending and inserting: {lst}') 

print() 

print('Pop and Remove') 

# Pop and Remove 
element = lst.pop(0) 
lst.remove(10.0) 

print(f'list after popping and removing : {lst}') 
print(f'pop function also returns the element : {element}') 
