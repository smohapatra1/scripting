# #   https://www.hackerrank.com/challenges/grid-walking/problem?isFullScreen=true

# You are situated in an  dimensional grid at position . The dimensions of the grid are . In one step, you can walk one step ahead or behind in any one of the  dimensions. This implies that there are always  possible moves if movements are unconstrained by grid boundaries. How many ways can you take  steps without leaving the grid at any point? You leave the grid if at any point , either  or .

# For example, you start off in a 3 dimensional grid at position . The dimensions of the grid are , so each of your axes will be numbered from  to . If you want to move  step, you can move to the following coordinates: .

# image

# If we started at  in the same grid, our new paths would lead to . Other moves are constrained by .

# Function Description

# Complete the gridWalking function in the editor below. It should return an integer that represents the number of possible moves, modulo .

# gridWalking has the following parameter(s):

# m: an integer that represents the number of steps
# x: an integer array where each  represents a coordinate in the  dimension where 
# D: an integer array where each  represents the upper limit of the axis in the  dimension
# Input Format

# The first line contains an integer , the number of test cases.

# Each of the next  sets of lines is as follows:

# The first line contains two space-separated integers,  and .
# The next line contains  space-separated integers .
# The third line of each test contains  space-separated integers .
# Constraints

# Output Format

# Output one line for each test case. Since the answer can be really huge, output it modulo .

# Sample Input

# 1
# 2 3
# 1 1
# 2 3
# Sample Output

# 12
# Explanation

# We are starting from (1, 1) in a  2-D grid, and need to count the number of possible paths with length equal to .

# Here are the  paths:















#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridWalking' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY D
#

def gridWalking(m, x, D):
    # Write your code here
    MOD = 10 ** 9 + 7
    n = len(D)
    md = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(n):
        M = [[0 for _ in range(m + 1)] for _ in range(D[i] + 1)]
        for j in range(1, D[i] + 1):
            M[j][0] = 1
        for j in range(1, m + 1):
            for k in range(1, D[i] + 1):
                M[k][j] = 0
                if k - 1 > 0:
                    M[k][j] = (M[k][j] + M[k - 1][j - 1]) % MOD;
                if k + 1 <= D[i]:
                    M[k][j] = (M[k][j] + M[k + 1][j - 1]) % MOD
        md[0][i + 1] = 1
        for j in range(1, m + 1):
            md[j][i + 1] = M[x[i]][j]
    c = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        c[i][0] = 1
        c[i][i] = 1
    for i in range(1, m + 1):
        for j in range(1, i):
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
    mdt = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        mdt[i][1] = md[i][1]
    for i in range(n + 1):
        mdt[0][i] = 1
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            mdt[j][i] = 0
            for k in range(j + 1):
                mdt[j][i] = (mdt[j][i] + ((c[j][j - k] * ((mdt[k][i - 1] * md[j - k][i]) % MOD)) % MOD)) % MOD
    return mdt[m][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        x = list(map(int, input().rstrip().split()))

        D = list(map(int, input().rstrip().split()))

        result = gridWalking(m, x, D)

        fptr.write(str(result) + '\n')

    fptr.close()
