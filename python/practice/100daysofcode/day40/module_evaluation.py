#Write a function that accepts a number  𝑥  and evaluates the following expression:

#𝑦=𝑎𝑏𝑠(𝑥3)+𝑐𝑜𝑠(3𝑥‾‾‾√) 
from math import *
def eval_exp(x):
    y = (abs(x**3) + cos(sqrt(3*x))
    print("Value :%s" % y)
eval_exp(input("Enter a number : "))
