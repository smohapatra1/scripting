# #   https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true

# Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

# Example


# She gives the students candy in the following minimal amounts: . She must buy a minimum of 10 candies.

# Function Description

# Complete the candies function in the editor below.

# candies has the following parameter(s):

# int n: the number of children in the class
# int arr[n]: the ratings of each student
# Returns

# int: the minimum number of candies Alice must buy
# Input Format

# The first line contains an integer, , the size of .
# Each of the next  lines contains an integer  indicating the rating of the student at position .

# Constraints

# Sample Input 0

# 3
# 1
# 2
# 2
# Sample Output 0

# 4
# Explanation 0

# Here 1, 2, 2 is the rating. Note that when two children have equal rating, they are allowed to have different number of candies. Hence optimal distribution will be 1, 2, 1.

# Sample Input 1

# 10
# 2
# 4
# 2
# 6
# 1
# 7
# 8
# 9
# 2
# 1
# Sample Output 1

# 19
# Explanation 1

# Optimal distribution will be 

# Sample Input 2

# 8
# 2
# 4
# 3
# 5
# 2
# 6
# 4
# 5
# Sample Output 2

# 12
# Explanation 2

# Optimal distribution will be .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Write your code here
    frwd = [1] * n 
    back = [1] * n 
    totl = [0] * n
    frwd[0] = 1
    back[-1] = 1 
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            frwd[i] = frwd[i-1] + 1 
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1]:
            back[i] = back[i+1]+1
    for i in range(len(arr)):
        totl[i] = max(frwd[i], back[i])
    return sum(totl)
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
