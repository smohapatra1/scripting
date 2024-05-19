# #   https://www.hackerrank.com/challenges/array-splitting/problem?isFullScreen=true

# Nikita just came up with a new array game. The rules are as follows:

# Initially, Nikita has an array of integers.

# In each move, Nikita must partition the array into  non-empty contiguous parts such that the sum of the elements in the left partition is equal to the sum of the elements in the right partition. If Nikita can make such a move, she gets  point; otherwise, the game ends.

# After each successful move, Nikita discards either the left partition or the right partition and continues playing by using the remaining partition as array .

# Nikita loves this game and wants your help getting the best score possible. Given , can you find and print the maximum number of points she can score?

# For example, Nikita starts with the array . She first splits it into  and , then discards . . Discard  leaving . This cannot be further split, so Nikita scored .

# Function Description

# Complete the arraySplitting function in the editor below. It should return an integer that reperesents the number of times Nikita can split the array.

# arraySplitting has the following parameter(s):

# arr: an array of integers
# Input Format

# The first line contains an integer , the number of test cases.

# Each of the next  pairs of lines is as follows:

# The first line contains an integer , the size of array .
# The next line contains  space-separated integers .
# Constraints

# Scoring

#  for  of the test data
#  for  of the test data
#  for  of the test data
# Output Format

# For each test case, print Nikita's maximum possible score on a new line.

# Sample Input

# 3
# 3
# 3 3 3
# 4
# 2 2 2 2
# 7
# 4 1 0 1 1 0 1
# Sample Output

# 0
# 2
# 3
# Explanation

# Test Case 0:

# Nikita cannot partition  into  parts having equal sums. Therefore, her maximum possible score is  and we print  on a new line.

# Test Case 1:

# Initially,  looks like this:
# split(3).png

# She splits the array into  partitions having equal sums, and then discards the left partition:

# split(1).png

# She then splits the new array into  partitions having equal sums, and then discards the left partition:

# split(2).png

# At this point the array only has  element and can no longer be partitioned, so the game ends. Because Nikita successfully split the array twice, she gets  points and we print  on a new line.

# Test Case 2:

# array		a1	a2
# [4,1,0,1,1,0,1]	[4]	[1,0,1,1,0,1]
# [1,0,1,1,0,1]	[1,0,1]	[1,0,1]
# [1,0,1]		[1,0]	[1]
# The answer is .



#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate

#
# Complete the 'arraySplitting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
cum = []
l = {}

def rec(i,j):
    m = cum[i-1]+((cum[j]-cum[i-1])/2)
    return 0 if m not in l else 1+max(rec(i,l[m]),rec(l[m]+1,j))
    
def arraySplitting(arr):
    # Write your code here
    global cum, l
    cum = list(accumulate(arr)) + [0]
    l = {cum[i]:i for i in range(len(cum)-1)} # lookup
    return len(arr)-1 if cum[-2]==0 else rec(0,len(arr)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = arraySplitting(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
