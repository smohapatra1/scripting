# #   https://www.hackerrank.com/challenges/problem-solving/problem

# There are N problems numbered 1..N which you need to complete. You've arranged the problems in increasing difficulty order, and the ith problem has estimated difficulty level i. You have also assigned a rating vi to each problem. Problems with similar vi values are similar in nature. On each day, you will choose a subset of the problems and solve them. You've decided that each subsequent problem solved on the day should be tougher than the previous problem you solved on that day. Also, to make it less boring, consecutive problems you solve should differ in their vi rating by at least K. What is the least number of days in which you can solve all problems?

# Input Format

# The first line contains the number of test cases T. T test cases follow. Each case contains an integer N and K on the first line, followed by integers v1,...,vn on the second line.

# Constraints

# 1 <= T <= 100
# 1 <= N <= 300
# 1 <= vi <= 1000
# 1 <= K <= 1000

# Output Format

# Output T lines, one for each test case, containing the minimum number of days in which all problems can be solved.

# Sample Input

# 2  
# 3 2  
# 5 4 7  
# 5 1  
# 5 3 4 5 6
# Sample Output

# 2  
# 1
# Explanation

# For the first example, you can solve the problems with rating 5 and 7 on the first day and the problem with rating 4 on the next day. Note that the problems with rating 5 and 4 cannot be completed consecutively because the ratings should differ by at least K (which is 2). Also, the problems cannot be completed in order 5,7,4 in one day because the problems solved on a day should be in increasing difficulty level.

# For the second example, all problems can be solved on the same day.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'problemSolving' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY v
#

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    vi = list(map(int, input().split()))

    m = [None] * N
    def match(s):
        if v[s]: return False
        v[s] = True
        for i in range(s+1, N):
            if abs(vi[i] - vi[s]) < K: continue
            if m[i] == None or match(m[i]):
                m[i] = s
                return True
        return False

    mc = 0
    for i in range(N):
        v = [False] * N
        if match(i): mc += 1
    print(N - mc)


# def problemSolving(k, v):
#     # Write your code here


# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     v = list(map(int, input().rstrip().split()))

#     result = problemSolving(k, v)
#     print (result)

#     # fptr.write(str(result) + '\n')

#     # fptr.close()
