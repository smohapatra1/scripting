# #   https://www.hackerrank.com/challenges/tower-breakers-again-1/problem?isFullScreen=true

# Two players (numbered  and ) are playing a game of Tower Breakers! The rules of the game are as follows:

# Player  always moves first.
# Initially there are  towers of various heights.
# The players move in alternating turns. In each turn, a player must choose a tower of height  and break it down into  towers, each of height . The numbers  and  must satisfy  and .
# If the current player is unable to make any move, they lose the game.
# Given the value of  and the respective height values for all towers, can you determine who will win, assuming both players always move optimally? If the first player wins, print ; otherwise, print .

# Input Format

# The first line contains an integer, , denoting the number of test cases.
# The  subsequent lines define the test cases. Each test case is described by two lines:

# An integer, , denoting the number of towers.
#  space-separated integers, , where each  describes the height of tower .
# Constraints

# Output Format

# For each test case, print a single integer denoting the winner (i.e., either  or ) on a new line.

# Sample Input

# 2
# 2 
# 1 2
# 3 
# 1 2 3
# Sample Output

# 1
# 2
# Explanation

# In the first test case, the first player simply breaks down the second tower of height  into two towers of height  and wins.

# In the second test case, there are only two possible moves:

# Break the second tower into  towers of height .
# Break the third tower into  towers of height .
# Whichever move player  makes, player  can make the other move and win the game.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from functools import reduce
def mex(s):
    f=0
    m=max(s)
    for i in range(m):
        if i not in s:
            return i
    return m+1
def factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def grundy(n):
    if n in [0,1]:
        return 0
    s={0}
    f=factors(n)-{1,n}
    for e in f:
        if e%2==1:
            s.add(grundy(int(n/e)))
    return mex(s)
t=int(input().strip())
for each in range(t):
    n=int(input().strip())
    arr=[int(i) for i in input().strip().split(" ")]
    g=grundy(arr[0])
    for i in range(1,n):
        #print(arr[i],grundy(arr[i]))
        g ^= grundy(arr[i])
    if g==0:
        print('2')
    else:
        print('1')

# def towerBreakers(arr):
#     # Write your code here
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         arr_count = int(input().strip())

#         arr = list(map(int, input().rstrip().split()))

#         result = towerBreakers(arr)

#         fptr.write(str(result) + '\n')

#     fptr.close()
