# #   https://www.hackerrank.com/challenges/equal/problem?isFullScreen=true

# Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.

# To make things difficult, she must equalize the number of chocolates in a series of operations. For each operation, she can give  pieces to all but one colleague. Everyone who gets a piece in a round receives the same number of pieces.

# Given a starting distribution, calculate the minimum number of operations needed so that every colleague has the same number of pieces.

# Example

#  represents the starting numbers of pieces for each colleague. She can give  pieces to the first two and the distribution is then . On the next round, she gives the same two  pieces each, and everyone has the same number: . Return the number of rounds, .

# Function Description

# Complete the equal function in the editor below.

# equal has the following parameter(s):

# int arr[n]: the integers to equalize
# Returns

# int: the minimum number of operations required
# Input Format

# The first line contains an integer , the number of test cases.

# Each test case has  lines.
# - The first line contains an integer , the number of colleagues and the size of .
# - The second line contains  space-separated integers, , the numbers of pieces of chocolate each colleague has at the start.

# Constraints



# The number of chocolates each colleague has initially < .

# Sample Input

# STDIN       Function
# -----       --------
# 1           t = 1
# 4           arr[] size n = 4
# 2 2 3 7     arr =[2, 2, 3, 7]
# Sample Output

# 2
# Explanation

# Start with 
# Add  to all but the 3rd element 
# Add  to all but the 4th element 

# Two operations were required.

# Sample Input 1

# 1
# 3
# 10 7 12
# Sample Output 1

# 3
# Explanation 1

# Start with 
# Add  to the first two elements 
# Add  to the last two elements 
# Add  to the last two elements 

# Three operations were required.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def min_oper(n,m):
    # min# of operation to reduce n to m
    if n==m:
        return 0
    oper1,rem=(n-m)//5,(n-m)%5
    oper2=0
    if rem==1 or rem==2:
        oper2=1
    elif rem==3 or rem==4:
        oper2=2
    return oper1+oper2

def equal(arr):
    # Write your code here
    arr.sort()
    dp=[[0]*5 for _ in range(len(arr))]
    for j in range(5):
        dp[0][j]=min_oper(arr[0],arr[0]-j)
    for i in range(1,len(arr)):
        for j in range(5):
            dp[i][j]=min_oper(arr[i],arr[0]-j)+dp[i-1][j]
    return min(dp[-1][j] for j in range(5))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
