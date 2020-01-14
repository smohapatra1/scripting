#Write a function to calculate average of a list
from math import *
def average_list(a):
# 1 way     
    l = len(a)
    print ("Length: ", l)
    c= 0 
    for i in a:
        c = c+i 
        i+=1
    av = c/l
    print (av)
    
#2nd way 
    #av = sum(a)/len(a)
    #print ("Average = ", round(av))
average_list([3,4])
