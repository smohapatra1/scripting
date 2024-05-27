# #   https://www.hackerrank.com/challenges/swappermutation/problem?isFullScreen=true

# You are given an array A = [1, 2, 3, ..., n]:

# How many sequences (S1) can you get after exact k adjacent swaps on A?

# How many sequences (S2) can you get after at most k swaps on A?

# An adjacent swap can be made between two elements of the Array A, A[i] and A[i+1] or A[i] and A[i-1].
# A swap otherwise can be between any two elements of the array A[i] and A[j] ∀ 1 ≤ i, j ≤ N, i ≠ j.

# Input Format

# First and only line contains n and k separated by space.

# Constraints

# 1 ≤ n ≤ 2500
# 1 ≤ k ≤ 2500

# Output Format

# Output S1 % MOD and S2 % MOD in one line, where MOD = 1000000007.

# Sample Input

# 3 2
# Sample Output

# 3 6
# Explanation

# Original array: [1, 2, 3]
# 1. After 2 adjacent swaps:
# We can get [1, 2, 3], [2, 3, 1], [3, 1, 2] ==> S1 == 3

# 2. After at most 2 swaps:
# 1) After 0 swap: [1, 2, 3]
# 2) After 1 swap: [2, 1, 3], [3, 2, 1], [1, 3, 2].
# 3) After 2 swaps: [1, 2, 3], [2, 3, 1], [3, 1, 2]
# ==> S2 == 6 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def swapPermutation(n, k):
    # Write your code here
    mod = 1000000007
    s = [1] + [0] * k
    t = [1] + [0] * k
    for i in range(1, n):
        temp = sum(s[max(k - i, 0):k]) % mod
        for j in range(k, 0, -1):
            s[j] = (s[j] + temp) % mod
            if j > i:
                temp = (temp + s[j - i - 1] - s[j - 1]) % mod
            else:
                temp = (temp - s[j - 1]) % mod
        for j in range(k, 0, -1):
            t[j] = (t[j] + i * t[j - 1]) % mod
    return sum(s[k % 2::2]) % mod, sum(t) % mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    result = swapPermutation(n, k)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
