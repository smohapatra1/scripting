# #   https://www.hackerrank.com/challenges/tower-breakers-revisited-1/problem?isFullScreen=true

# Two players (numbered  and ) are playing a game of Tower Breakers! The rules of the game are as follows:

# Player  always moves first, and both players always move optimally.
# Initially there are  towers of various heights.
# The players move in alternating turns. In each turn, a player can choose a tower of height  and reduce its height to , where  and  evenly divides .
# If the current player is unable to make any move, they lose the game.
# Given the value of  and the respective height values for all towers, can you determine who will win? If the first player wins, print ; otherwise, print .

# Input Format

# The first line contains an integer, , denoting the number of test cases.
# Each of the  subsequent lines defines a test case. Each test case is described over the following two lines:

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

# Test Case 0:
# Player  reduces the second tower to height  and subsequently wins.

# Test Case 1:
# There are two possible moves:

# Reduce the second tower to 
# Reduce the third tower to .
# Whichever move player  makes, player  will make the other move. Thus, player  wins.


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

from math import sqrt 

def pFactors(n):        
    pFact,limit,check,num=[],int(sqrt(n))+1,2,n 
    if n==1: return [] 
    for check in range(2, limit): 
        while num%check==0: 
            pFact.append(check) 
            num//=check 
    if num>1: 
        pFact.append(num) 
    return pFact 

t=int(input())
for x in range(t):
    n=int(input())
    a=[len(pFactors(int(y))) for y in input().strip().split(' ')]
    xor=0
    for y in a: xor=xor^y
    if xor==0:      print(2)
    else:           print(1)  

# def towerBreakers(arr):
#     # Write your code here
#     result=arr[0]
#     for i in range(1, len(arr)):
#         result ^= arr[i]
#     if result !=0:
#         return '1'
#     else:
#         return '2'

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         arr_count = int(input().strip())

#         arr = list(map(int, input().rstrip().split()))

#         result = towerBreakers(arr)

#         fptr.write(str(result) + '\n')

#     fptr.close()
