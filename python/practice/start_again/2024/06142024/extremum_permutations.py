# #   https://www.hackerrank.com/challenges/extremum-permutations/problem?isFullScreen=true

# Let's consider a permutation P = {p1, p2, ..., pN} of the set of N = {1, 2, 3, ..., N} elements .

# P is called a magic set if it satisfies both of the following constraints:

# Given a set of K integers, the elements in positions a1, a2, ..., aK are less than their adjacent elements, i.e., pai-1 > pai < pai+1
# Given a set of L integers, elements in positions b1, b2, ..., bL are greater than their adjacent elements, i.e., pbi-1 < pbi > pbi+1
# How many such magic sets are there?

# Input Format
# The first line of input contains three integers N, K, L separated by a single space.
# The second line contains K integers, a1, a2, ... aK each separated by single space.
# the third line contains L integers, b1, b2, ... bL each separated by single space.

# Output Format
# Output the answer modulo 1000000007 (109+7).

# Constraints
# 3 <= N <= 5000
# 1 <= K, L <= 5000
# 2 <= ai, bj <= N-1, where i ∈ [1, K] AND j ∈ [1, L]

# Sample Input #00

# 4 1 1
# 2
# 3
# Sample Output #00

# 5
# Explanation #00

# Here, N = 4 a1 = 2 and b1 = 3. The 5 permutations of {1,2,3,4} that satisfy the condition are

# 2 1 4 3
# 3 2 4 1
# 4 2 3 1
# 3 1 4 2
# 4 1 3 2
# Sample Input #01

# 10 2 2
# 2 4
# 3 9
# Sample Output #01

# 161280

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extremumPermutations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

N, K, L = map(int,input().split())
mins = list(map(int, input().split()))
maxs = list(map(int, input().split()))

M = int(1e9 + 7)
ANY = 0
UP = 1
DOWN = -1
direction = [0] * (N + 1)

for i in mins:
    if direction[i - 1] == UP or direction[i] == DOWN:
        print("0")
        sys.exit(0)
    direction[i - 1] = DOWN
    direction[i] = UP
for i in maxs:
    if direction[i - 1] == DOWN or direction[i] == UP:
        print("0")
        sys.exit(0)
    direction[i - 1] = UP
    direction[i] = DOWN
f = []
for i in range(N + 1):
    f.append([0] * (N + 1))

def interval(a, b):
    if a <= b:
        return range(a, b + 1)
    else:
        return range(a, b - 1, -1)

f[N][0] = 1
i = N - 1
while i > 0:
    if direction[i] == UP:
        f[i][0] = 0
        for n in interval(1, N - i):
            f[i][n] = (f[i][n - 1] + f[i + 1][n - 1]) % M       
    elif direction[i] == DOWN:
        f[i][N - i] = 0
        for n in interval(N - i - 1, 0):
            m = N - i - n
            f[i][n] = (f[i][n + 1] + f[i + 1][n]) % M  
    elif direction[i] == ANY:
        s = 0
        for k in interval(0, N - (i + 1)):
            s += f[i + 1][k]
            s %= M
        for n in interval(0, N - i):
            f[i][n] = s
    i -= 1

ret = 0
for k in interval(0, N - 1):
    ret += f[1][k]
    ret %= M
print(ret)

# def extremumPermutations(n, a, b):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     l = int(first_multiple_input[2])

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = extremumPermutations(n, a, b)

#     fptr.write(str(result) + '\n')

#     fptr.close()

