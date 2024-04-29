# #   https://www.hackerrank.com/challenges/build-a-string/problem?isFullScreen=true

# Greg wants to build a string,  of length . Starting with an empty string, he can perform  operations:

# Add a character to the end of  for  dollars.
# Copy any substring of , and then add it to the end of  for  dollars.
# Calculate minimum amount of money Greg needs to build .

# Input Format

# The first line contains number of testcases .

# The  subsequent lines each describe a test case over  lines:
# The first contains  space-separated integers, ,  , and , respectively.
# The second contains  (the string Greg wishes to build).

# Constraints

#  is composed of lowercase letters only.
# Output Format

# On a single line for each test case, print the minimum cost (as an integer) to build .

# Sample Input

# 2
# 9 4 5
# aabaacaba
# 9 8 9
# bacbacacb
# Sample Output

# 26
# 42
# Explanation

# Test Case 0:
#  "";  ""
# Append "";  ""; cost is 
# Append "";  ""; cost is 
# Append "";  ""; cost is 
# Copy and append "";  ""; cost is 
# Append "";  ""; cost is 
# Copy and append "";  ""; cost is 

# Summing each cost, we get , so our output for Test Case 1 is .

# Test Case 1:
#  "";  ""
# Append "";  ""; cost is 
# Append "";  ""; cost is 
# Append "";  ""; cost is 
# Copy and append "";  ""; cost is 
# Copy and append "";  ""; cost is 

# Summing each cost, we get , so our output for Test Case 2 is .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'buildString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. STRING s
#

def buildString(a, b, s):
    # Write your code here
    N = len(s)

    cost = [0]*N

    cost[0] = a
    index = 1
    for i in range(1,N):
        if s[index:i+1] not in s[:index] or index == -1:
            index = findLongestOccurence(s[:i+1], i)
        if index==-1:
            cost[i] = cost[i-1] + a
        else:
            cost[i] = min(cost[i-1]+a, cost[index-1]+b)
    return cost[-1]

def findLongestOccurence(s, index):
    indexHasChanged = False
    while s[index:] in s[:index]:
        index -= 1
        indexHasChanged = True
    return -1 if not indexHasChanged else index + 1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        s = input()

        result = buildString(a, b, s)
        
        fptr.write(str(result) + '\n')

    fptr.close()

