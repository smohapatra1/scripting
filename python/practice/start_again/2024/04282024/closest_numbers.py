# #   https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true

# Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

# Example

# Sorted, . Several pairs have the minimum difference of : . Return the array .

# Note
# As shown in the example, pairs may overlap.

# Given a list of unsorted integers, , find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.

# Function Description

# Complete the closestNumbers function in the editor below.

# closestNumbers has the following parameter(s):

# int arr[n]: an array of integers
# Returns
# - int[]: an array of integers as described

# Input Format

# The first line contains a single integer , the length of .
# The second line contains  space-separated integers, .

# Constraints

# All  are unique in .
# Output Format

# Sample Input 0

# 10
# -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 
# Sample Output 0

# -20 30
# Explanation 0
# (30) - (-20) = 50, which is the smallest difference.

# Sample Input 1

# 12
# -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 
# Sample Output 1

# -520 -470 -20 30
# Explanation 1
# (-470) - (-520) = 30 - (-20) = 50, which is the smallest difference.

# Sample Input 2

# 4
# 5 4 3 2
# Sample Output 2

# 2 3 3 4 4 5
# Explanation 2
# Here, the minimum difference is 1. Valid pairs are (2, 3), (3, 4), and (4, 5).


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    diff = arr[1] - arr[0]
    minArr = []
    for i in range(0, len(arr)-1):
        if arr[i+1]-arr[i] == diff:
            minArr.extend([arr[i], arr[i+1]])
        elif arr[i+1]-arr[i] < diff:
            diff = arr[i+1]-arr[i]
            minArr.clear()
            minArr.extend([arr[i], arr[i+1]])
    return minArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
