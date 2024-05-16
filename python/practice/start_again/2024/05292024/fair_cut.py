# #   https://www.hackerrank.com/challenges/fair-cut/problem?isFullScreen=true

# Li and Lu have  integers, , that they want to divide fairly between the two of them. They decide that if Li gets integers with indices  (which implies that Lu gets integers with indices ), then the measure of unfairness of this division is:

# Find the minimum measure of unfairness that can be obtained with some division of the set of integers where Li gets exactly  integers.

# Note  means Set complement

# Input Format

# The first line contains two space-separated integers denoting the respective values of  (the number of integers Li and Lu have) and  (the number of integers Li wants).
# The second line contains  space-separated integers describing the respective values of .

# Constraints

# For  of the test cases, .
# For  of the test cases, .
# Output Format

# Print a single integer denoting the minimum measure of unfairness of some division where Li gets  integers.

# Sample Input 0

# 4 2
# 4 3 1 2
# Sample Output 0

#  6
# Explanation 0
# One possible solution for this input is . 

# Sample Input 1

# 4 1
# 3 3 3 1
# Sample Output 1

# 2
# Explanation 1
# The following division of numbers is optimal for this input: .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#



def fairCut(k, arr):
    # Write your code here
    k = n - k if k > n//2 else k
    arr.sort()
    measure = []
    for _ in range(n + 1):
        measure.append([float('inf')] * (k + 1))

    measure[0][0] = 0

    for i in range(1, n + 1):
        a_i = arr[i - 1]
        measure[i][0] = measure[i-1][0] - a_i * k
    for i in range(1, n + 1):
        for j in range(1, min(k + 1, i + 1)):
            a_i = arr[i-1]
            # if we put a_i in X
            measure_X = measure[i-1][j-1] \
                - a_i * ((n - k) - (i - j)) \
                + a_i * (i - j)

            # if we put a_i in Y
            measure_Y = measure[i-1][j] \
                - a_i * (k - j) \
                + a_i * (j)

            measure[i][j] = min(measure_X, measure_Y)
    return measure[n][k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
