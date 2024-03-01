#   https://www.hackerrank.com/test/3fmlgi1ase7/questions/38ja2jois2r

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    min_Value=max(a)
    max_Value=min(b)
    start_Value=min_Value
    result=[]
    while start_Value <=max_Value:
        if all ([start_Value % x == 0 for x in a ]) and all([x % start_Value == 0  for x in b]):
            result.append(start_Value)
        start_Value +=min_Value
    return len(result)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print (total)
    # fptr.write(str(total) + '\n')
    # fptr.close()
