# Define a function named minimunm_difference with is taking 3 parameters
# Calcilate the difference between each pairs and rerurn minimum of these differences 
import math
def minimum_difference(a,b,c):
    #Calculate the first difference and use of absolute values ( abs )
    first_diff = abs(a - b )
    second_diff = abs(b - c )
    third_diff = abs(c - a )
    d = min(first_diff, second_diff, third_diff)
    print (f'{d}')
    #print (f' min({first_diff} , {second_diff}, {third_diff} )')
minimum_difference( int(18), int(5), int(10) )
