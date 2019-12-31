#!/usr/bin/python
# A program to determine if a number is prime
number = int(input("Enter a number : "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print ("%d is not prime" %number)
            break
    else:
        print ("%d is prime" %number)
#else:
#    print ("%d is not prime" % number)
        
