#   https://www.hackerrank.com/test/4j8jqbol4g4/questions/g2lt30pl1g0

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    dict={}
    result=0
    for ele in arr:
        dict[ele] =1
        if ele+k in dict:
            result+=1
        if ele -k in dict:
            result +=1
    return result
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    print (result)

    # fptr.write(str(result) + '\n')

    # fptr.close()

