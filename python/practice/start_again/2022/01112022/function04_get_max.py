#Get max of three integers using functions
import math
def get_max(a,b,c):
    """ Normal Way"""
    if a > b and a > c  :
        print (f'Max number is : {a}')
    elif b > a and b > c :
        print (f'Max number is : {b}')
    elif c > a and c > b :
        print (f'Max number is : {c}')
    """ Using math/Max function """
    print (f'Max number using max function: {max(a,b,c)}')

get_max(int(input("Enter the valus of a: ")), 
        int(input("Enter the value of b: ")),
        int(input("Enter the value of c: "))) 




