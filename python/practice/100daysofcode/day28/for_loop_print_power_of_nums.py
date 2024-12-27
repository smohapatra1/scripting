#!/usr/bin/python
#Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines. For example if 'n' is equal to 4 then the output should look like the following:
a = int(input("Enter a number "))
count = 0
for i in range(count, a+1 ):
    #i +=1
    i = 10**i
    print (i)
    #count +=1
        
