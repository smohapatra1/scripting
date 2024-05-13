# #   https://www.hackerrank.com/challenges/sherlock-and-cost/problem?isFullScreen=true

# In this challenge, you will be given an array  and must determine an array . There is a special rule: For all , . That is,  can be any number you choose such that . Your task is to select a series of  given  such that the sum of the absolute difference of consecutive pairs of  is maximized. This will be the array's cost, and will be represented by the variable  below.

# The equation can be written:

# For example, if the array , we know that , , and . Arrays meeting those guidelines are:

# [1,1,1], [1,1,2], [1,1,3]
# [1,2,1], [1,2,2], [1,2,3]
# Our calculations for the arrays are as follows:

# |1-1| + |1-1| = 0	|1-1| + |2-1| = 1	|1-1| + |3-1| = 2
# |2-1| + |1-2| = 2	|2-1| + |2-2| = 1	|2-1| + |3-2| = 2
# The maximum value obtained is .

# Function Description

# Complete the cost function in the editor below. It should return the maximum value that can be obtained.

# cost has the following parameter(s):

# B: an array of integers
# Input Format

# The first line contains the integer , the number of test cases.

# Each of the next  pairs of lines is a test case where:
# - The first line contains an integer , the length of 
# - The next line contains  space-separated integers 

# Constraints

# Output Format

# For each test case, print the maximum sum on a separate line.

# Sample Input

# 1
# 5
# 10 1 10 1 10
# Sample Output

# 36
# Explanation

# The maximum sum occurs when A[1]=A[3]=A[5]=10 and A[2]=A[4]=1. That is .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # Write your code here
    suma = 0
    sumb = 0
    for i in range(len(B)):
        if i == 0:
            a = B[i]
            b = 1
        if i != 0:
            a = max([sumb + B[i] - 1, suma + abs(B[i] - B[i-1])])
            b = suma + abs(1 - B[i-1])
            suma = a
            sumb = b

    return(max([suma, sumb]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
