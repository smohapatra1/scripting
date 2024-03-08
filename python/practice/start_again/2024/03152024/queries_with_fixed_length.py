# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-queries-with-fixed-length/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four

# Consider an -integer sequence, . We perform a query on  by using an integer, , to calculate the result of the following expression:

# In other words, if we let , then you need to calculate .

# Given  and  queries, return a list of answers to each query.

# Example


# The first query uses all of the subarrays of length : . The maxima of the subarrays are . The minimum of these is .

# The second query uses all of the subarrays of length : . The maxima of the subarrays are . The minimum of these is .

# Return .

# Function Description

# Complete the solve function below.

# solve has the following parameter(s):

# int arr[n]: an array of integers
# int queries[q]: the lengths of subarrays to query
# Returns

# int[q]: the answers to each query
# Input Format

# The first line consists of two space-separated integers,  and .
# The second line consists of  space-separated integers, the elements of .
# Each of the  subsequent lines contains a single integer denoting the value of  for that query.

# Constraints

# Sample Input

# 5 5
# 1 2 3 4 5
# 1
# 2
# 3
# 4
# 5
# Sample Output

# 1
# 2
# 3
# 4
# 5
# Explanation

# Each prefix has the least maximum value among the consecutive subsequences of the same size.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    n=len(arr)
    minimums=[]
    for d in queries:
        maximum = minimum = max(arr[0:d])
        for i in range(1, n-d + 1):
            if arr[i + d - 1 ] > maximum:
                maximum = arr[i+d -1]
            elif arr[i-1] == maximum :
                maximum = max(arr[i:i+d])
            if maximum < minimum:
                minimum = maximum
        minimums.append(minimum)
    return minimums
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
