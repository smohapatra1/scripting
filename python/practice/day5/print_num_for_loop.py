#!/usr/bin/python
#Print Even numbers from a range 
print ("Using range function")

for i in range(1,11):
    print (i)
#Increment of two
print "Increment of numbers..."
for i in range(0,20,2):
    print (i)
#Odd
print "Printing odd numbers..."
for i in range(1,10):
    if (i % 2 ) == 0 :
        print ("%d is even") % i
    else:
        print ("%d is odd") % i 
#Multiplication of 5
print ("Multiplication of 5")
for i in range (0,11):
    print (i*5)
print ("Multiplication of 5.....")
for i in range (0,51,5):
    print (i)

#Nested for loops
print ("Nested for loops")
for i in range(1,5):
    for j in range(1,3):
        print (i*j)
