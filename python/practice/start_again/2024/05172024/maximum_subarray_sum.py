# #   https://www.hackerrank.com/challenges/maximum-subarray-sum/problem?isFullScreen=true

# We define the following:

# A subarray of array  of length  is a contiguous segment from  through  where .
# The sum of an array is the sum of its elements.
# Given an  element array of integers, , and an integer, , determine the maximum value of the sum of any of its subarrays modulo .

# Example


# The following table lists all subarrays and their moduli:

# 		sum	%2
# [1]		1	1
# [2]		2	0
# [3]		3	1
# [1,2]		3	1
# [2,3]		5	1
# [1,2,3]		6	0
# The maximum modulus is .

# Function Description

# Complete the maximumSum function in the editor below.

# maximumSum has the following parameter(s):

# long a[n]: the array to analyze
# long m: the modulo divisor
# Returns
# - long: the maximum (subarray sum modulo )

# Input Format

# The first line contains an integer , the number of queries to perform.

# The next  pairs of lines are as follows:

# The first line contains two space-separated integers  and (long), the length of  and the modulo divisor.
# The second line contains  space-separated long integers .
# Constraints

#  the sum of  over all test cases 
# Sample Input

# STDIN       Function
# -----       --------
# 1           q = 1
# 5 7         a[] size n = 5, m = 7
# 3 3 9 9 5
# Sample Output

# 6
# Explanation

# The subarrays of array  and their respective sums modulo  are ranked in order of length and sum in the following list:

#  and 
#  and 






# The maximum value for  for any subarray is .



#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    p = [0]
    for x in a:
        p.append((p[-1]+x)%m)
    d = m - max(p)
    pre = [0]
    for j in range(1, len(a)+1):
        if p[j] < pre[-1]:
            i = bisect_right(pre, p[j])
            d = min(d, pre[i]-p[j])
            pre.insert(i, p[j])
        else:
            pre.append(p[j])
    return m-d
      
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
