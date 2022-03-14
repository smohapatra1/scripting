#Calculate the arithmetic mean 
import math
def arithmetic_mean(*args):
    Sum=sum(args)
    print (f'{Sum}')
    num_of_elements=len(args)
    mean=Sum/num_of_elements
    print (f'{mean}')

arithmetic_mean(int(1,2))