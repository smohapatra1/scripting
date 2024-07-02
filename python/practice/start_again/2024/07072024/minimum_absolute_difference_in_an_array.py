# #   https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

# The absolute difference is the positive difference between two values  and , is written  or  and they are equal. If  and , . Given an array of integers, find the minimum absolute difference between any two elements in the array.

# Example. 

# There are  pairs of numbers:  and . The absolute differences for these pairs are ,  and . The minimum absolute difference is .

# Function Description

# Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

# minimumAbsoluteDifference has the following parameter(s):

# int arr[n]: an array of integers
# Returns

# int: the minimum absolute difference found
# Input Format

# The first line contains a single integer , the size of .
# The second line contains  space-separated integers, .

# Constraints

# Sample Input 0

# 3
# 3 -7 0
# Sample Output 0

# 3
# Explanation 0

# The first line of input is the number of array elements. The array,  There are three pairs to test: , , and . The absolute differences are:

# Remember that the order of values in the subtraction does not influence the result. The smallest of these absolute differences is .

# Sample Input 1

# 10
# -59 -36 -13 1 -53 -92 -2 -96 -54 75
# Sample Output 1

# 1
# Explanation 1

# The smallest absolute difference is .

# Sample Input 2

# 5
# 1 -3 71 68 17
# Sample Output 2

# 3
# Explanation 2

# The minimum absolute difference is .



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    diff = []
    arr.sort()
    for i in range(len(arr)-1):
        diff.append(abs(arr[i] - arr[i+1]))
    return min(diff)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
