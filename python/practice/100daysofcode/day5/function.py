#!/usr/bin/python

#Functions to get sum of two numbers

#Predefined and getting sum 
def input(a, b):
    c = int(a + b )
    print ("First number :- %d and 2nd :- % d and SUM :- %d") % (a, b, c)    
#Sum of two numbers
def sum():
    a = int(raw_input("Enter first num:  "))
    b = int(raw_input("Enter 2nd num: "))
    sum = a + b
    print ("Sum total : %d ") % sum
def retunAdd(a, b):
    return (a + b)

input(5, 6)
sum()
sum=retunAdd(10, 20)
print ("Return : % d ") % sum
