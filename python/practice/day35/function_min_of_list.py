#Write a function which accepts an input list of numbers and returns the smallest number in the list (use python's built-in min() function).
import os
def min_num(n):
    for i in n:
        b = min(n)
        c = max(n)
    print ("min - %d \nmax - %d " % (b, c))
min_num([1,2,3,4])
