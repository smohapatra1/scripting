#Write a function that accepts a number  𝑥  and evaluates the following expression:

#𝑦=𝑠𝑖𝑛(𝑥)−𝑐𝑜𝑠(𝑥)+𝑠𝑖𝑛(𝑥)𝑐𝑜𝑠(𝑥) 
from math import *
def trig (x):
    #y = math.sin(x) - math.cos(x) + math.sin(x) * math.cos(x)
    y = sin(x) - cos(x) + sin(x) * cos(x)
    print (float(y))

trig(int(input("Enter the value : ")))
