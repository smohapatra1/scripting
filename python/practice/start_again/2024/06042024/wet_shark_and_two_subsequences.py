# #   https://www.hackerrank.com/challenges/wet-shark-and-two-subsequences/problem?isFullScreen=true

# One day, Wet Shark was given an array . As always, he started playing with its subsequences.

# When you came to know about this habit, you presented him a task of finding all pairs of subsequences, , which satisfies all of the following constraints. We will represent a pair of subsequence as  and 

#  and  must be of same length, i.e., .
# Please help Wet Shark determine how many possible subsequences  and  can exist. Because the number of choices may be big, output your answer modulo .

# Note:

# Two segments are different if there's exists at least one index  such that element  is present in exactly one of them.
# Both subsequences can overlap each other.
# Subsequences do not necessarily have to be distinct
# Input Format

# The first line consists of 3 space-separated integers , , , where  denotes the length of the original array, , and  and  are as defined above.
# The next line contains  space-separated integers,  , representing the elements of .

# Constraints

# Output Format

# Output total number of pairs of subsequences, , satisfying the above conditions. As the number can be large, output it's modulo 

# Sample Input 0

# 4 5 3
# 1 1 1 4
# Sample Output 0

# 3
# Explanation 0

# For array  there are three pairs of subsequences:



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER r
#  3. INTEGER s
#

def twoSubsequences(x, r, s):
    # Write your code here
    m = len(x)
    mod = 10**9 + 7
    h, l = (r+s) //2, (r-s)//2
    result = 0 
    dp = [[0 for i in range(m+1)] for j in range(h+1)]
    dp [0][0] = 1 
    if x[0] <= h :
        dp[x[0]][1] = 1 
    for i in range(1, m ):
        for k in range(1, m+1):
            dp[0][k] = 0
        for j in range(h, 0, -1):
            dp[j][0] = 0
            for k in range(1, m+1):
                if j < x[i]:
                    dp[j][k] = dp[j][k]
                else:
                    dp[j][k] = (dp[j - x[i]][k - 1] + dp[j][k]) % mod
    if l >= 0 and (r+s) % 2 != 1 and (r-s) % 2 != 1 and r != 0:
        for i in range(m):
            result = (result + (dp[h][i] * dp[l][i])) % mod 
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    x = list(map(int, input().rstrip().split()))

    result = twoSubsequences(x, r, s)

    fptr.write(str(result) + '\n')

    fptr.close()
