#!/usr/bin/python
#Using a for loop, write a program which asks the user to type a positive integer, n, and then prints the sum of the square of all numbers form 1 to n (including both 1 and n).
a = int(input("Enter a number : "))
count = 1 
for i in range(count, a ):
    i +=1
    i = i ** 2
    count = count + i 
print (count)
