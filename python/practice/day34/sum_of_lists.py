#/usr/bin/python
import os
import sys
#Write a function that accepts a list of integers and returns the sum of all the numbers in the list. Assume that the input list contains only numbers. Do NOT use the built-in sum() function.
def my_list(lists):
    count = 0
    for i in lists:
        count = count + i 
        #i+=1
    print (count)        
my_list([1,2,3,4])

