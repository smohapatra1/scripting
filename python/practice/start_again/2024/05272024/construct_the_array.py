# #   https://www.hackerrank.com/challenges/construct-the-array/problem?isFullScreen=true

# Your goal is to find the number of ways to construct an array such that consecutive positions contain different values.

# Specifically, we want to construct an array with  elements such that each element between  and , inclusive. We also want the first and last elements of the array to be  and .

# Given ,  and , find the number of ways to construct such an array. Since the answer may be large, only find it modulo .

# For example, for , , , there are  ways, as shown here:

# image

# Complete the function countArray which takes input ,  and . Return the number of ways to construct the array such that consecutive elements are distinct.

# Constraints

# Subtasks

# For  of the maximum score,  and 
# Sample Input

# , , 

# Sample Output


# Explanation

# Refer to the diagram in the challenge statement.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    mod = 10 ** 9 + 7 
    if x == 1 :
        x_is = 1
        x_isnot = 0
    else:
        x_is = 0 
        x_isnot = 1 
    for i in range(2, n):
        x_is_temp = x_isnot 
        x_isnot = (x_is*(k-1) + x_isnot*(k-2 )) % mod 
        x_is = x_is_temp
    return x_isnot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
