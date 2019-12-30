#!/usr/bin/python
#Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.
count = 0
for i in range (1, 101):
    if i % 2 == 0 :
        count = count + i 
        i +=1
print (count)
