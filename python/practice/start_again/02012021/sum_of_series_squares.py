#Python Program to calculate Sum of Series 1²+2²+3²+….+n²
#Write a Python Program to calculate Sum of Series 1²+2²+3²+….+n² using For Loop and Functions with an example.
#The Mathematical formula for Python Sum of series 1²+2²+3²+….+n² = ( n (n+1) (2n+1)) / 6
import math

def sum_of_Series(n):
    
    total = 0 
    total = (n* (n +1)*(2*n +1))/6
    print ("sum_total = ", total )

n = int(input("Input the number for series "))
sum_of_Series(n)