#Define a function with input as a paramerter
#Calculate the logarithm of that paramter

import math
def get_logarithm(a):
    b=math.log(a)
    print (f'Logarithm of {a} is {b}')
get_logarithm(int(input("Enter the value: ")))