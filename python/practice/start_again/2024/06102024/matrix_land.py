# #   https://www.hackerrank.com/challenges/matrix-land/problem?isFullScreen=true

# You are playing a matrix-based game with the following setup and rules:

# You are given a matrix  with  rows and  columns. Each cell contains some points. When a player passes a cell their score increases by the number written in that cell and the number in the cell becomes . (If the cell number is positive their score increases, otherwise it decreases.)
# The player starts from any cell in the first row and can move left, right or down.
# The game is over when the player reaches the last row and stops moving.
# image

# Print the maximum score that the player can get.

# Input Format

# The first line contains  and . The next  lines contain  numbers each,  number in  line denotes the number that is written on cell .

# Constraints

# Subtasks

# for  tests .
# for  tests .
# Output Format

# Print the maximum score that the player can get.

# Sample Input 0

# 4 5
# 1 2 3 -1 -2
# -5 -8 -1 2 -150
# 1 2 3 -250 100
# 1 1 1 1 20
# Sample Output 0

# 37
# Explanation 0

# Refer the image given in statement, the path followed is  summing upto .
# Note that,  is traversed  times, but the second time it only contributes  to the sum.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixLand' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def matrixLand(A):
    # Write your code here
    width=len(A[0])
    if width==1:
        return sum(A[i][0] for i in range(len(A)))
    prevline=[0]*width
    for row in A:
        go_right=[0]*width
        go_left=[0]*width
        top,notop=-4000001,0
        for i in range(width):
            notop=max(0,notop)
            go_right[i]+=notop
            notop+=row[i]
            top=max(top+row[i],prevline[i]+notop)
            go_left[i]+=top
        top,notop=-4000001,0  
               
        for i in range(width-1,-1,-1):
           notop=max(0,notop)
           go_left[i]+=notop
           notop+=row[i]
           top=max(top+row[i],prevline[i]+notop)
           go_right[i]+=top
        for i in range(width):
            prevline[i]=max(go_left[i],go_right[i])
    return max(prevline)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    A = []

    for _ in range(n):
        A.append(list(map(int, input().rstrip().split())))

    result = matrixLand(A)

    fptr.write(str(result) + '\n')

    fptr.close()
