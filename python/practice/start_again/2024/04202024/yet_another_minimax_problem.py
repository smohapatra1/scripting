# #   https://www.hackerrank.com/challenges/yet-another-minimax-problem/problem?isFullScreen=true

# You are given  non-negative integers, . We define the score for some permutation () of length  to be the maximum of  for .

# Find the permutation with the minimum possible score and print its score.

# Note:  is the exclusive-OR (XOR) operator.

# Input Format

# The first line contains single integer, , denoting the number of integers.
# The second line contains  space-separated integers, , describing the respective integers.

# Constraints

# Output Format

# Print a single integer denoting the minimum possible score.

# Sample Input 0

# 4
# 1 2 3 4
# Sample Output 0

# 5
# Sample Input 1

# 3
# 1 2 3
# Sample Output 1

# 2
# Explanation

# Sample Case 0:
# The permutation with the minimum score is :



# Because the permutation's score is the maximum of these values, we print  on a new line.

# Sample Case 1:
# The permutation with the minimum score is :


# Because the permutation's score is the maximum of these values, we print  on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anotherMinimaxProblem' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def anotherMinimaxProblem(a):
    # Write your code here
    if all(x==0 for x in a ):
        return 0
    n = len(a)
    max_bit = max(a).bit_length()
    for bit in range(max_bit - 1, -1 , -1):
        ones, zeros = [], []
        for num in a :
            if num & (1 << bit):
                ones.append(num)
            else:
                zeros.append(num)
        if zeros and ones:
            break
    if not zeros and ones:
        return min(a[i] ^ a[j] for i in range(n) for j in range(i+1, n ))
    return min(x^y for x in zeros for y in ones)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = anotherMinimaxProblem(a)

    fptr.write(str(result) + '\n')

    fptr.close()
