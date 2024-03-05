#   https://www.hackerrank.com/test/4j8jqbol4g4/questions/6sqmn1811gk


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    positions=0
    fuel=0
    for i in range(len(petrolpumps)):
        fuel+=petrolpumps[i][0] - petrolpumps[i][1]
        if fuel < 0:
            fuel = 0 
            positions =i+1
    return positions
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
    print (result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
