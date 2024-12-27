#Write a function that accepts a number  𝑥  and evaluates the following polynomial expression:
#𝑦=𝑥4−12𝑥3+13𝑥2+11 
#and returns the value of y
import os
def eval_exp(x):
    y=(x**4 - 12* x**3 + 13* x**2 + 11 )
    print (y)
eval_exp(int(input("Enter a value of x ")))
