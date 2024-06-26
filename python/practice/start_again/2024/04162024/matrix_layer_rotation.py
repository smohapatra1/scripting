# #   https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=false

# You are given a 2D matrix of dimension  and a positive integer . You have to rotate the matrix  times and print the resultant matrix. Rotation should be in anti-clockwise direction.

# Rotation of a  matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only.

# matrix-rotation

# It is guaranteed that the minimum of m and n will be even.

# As an example rotate the Start matrix by 2:

#     Start         First           Second
#      1 2 3 4       2  3  4  5      3  4  5  6
#     12 1 2 5  ->   1  2  3  6 ->   2  3  4  7
#     11 4 3 6      12  1  4  7      1  2  1  8
#     10 9 8 7      11 10  9  8     12 11 10  9
# Function Description

# Complete the matrixRotation function in the editor below.

# matrixRotation has the following parameter(s):

# int matrix[m][n]: a 2D array of integers
# int r: the rotation factor
# Prints
# It should print the resultant 2D integer array and return nothing. Print each row on a separate line as space-separated integers.

# Input Format

# The first line contains three space separated integers, , , and , the number of rows and columns in , and the required rotation.
# The next  lines contain  space-separated integers representing the elements of a row of .

# Constraints





# Sample Input

# Sample Input #01

# STDIN        Function
# -----        --------
# 4 4 2        rows m = 4, columns n = 4, rotation factor r = 2
# 1 2 3 4      matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Sample Output #01

# 3 4 8 12
# 2 11 10 16
# 1 7 6 15
# 5 9 13 14
# Explanation #01

# The matrix is rotated through two rotations.

#      1  2  3  4      2  3  4  8      3  4  8 12
#      5  6  7  8      1  7 11 12      2 11 10 16
#      9 10 11 12  ->  5  6 10 16  ->  1  7  6 15
#     13 14 15 16      9 13 14 15      5  9 13 14
# Sample Input #02

# 5 4 7
# 1 2 3 4
# 7 8 9 10
# 13 14 15 16
# 19 20 21 22
# 25 26 27 28
# Sample Output #02

# 28 27 26 25
# 22 9 15 19
# 16 8 21 13
# 10 14 20 7
# 4 3 2 1
# Explanation 02

# The various states through 7 rotations:

#     1  2  3  4      2  3  4 10    3  4 10 16    4 10 16 22
#     7  8  9 10      1  9 15 16    2 15 21 22    3 21 20 28
#     13 14 15 16 ->  7  8 21 22 -> 1  9 20 28 -> 2 15 14 27 ->
#     19 20 21 22    13 14 20 28    7  8 14 27    1  9  8 26
#     25 26 27 28    19 25 26 27    13 19 25 26   7 13 19 25

#     10 16 22 28    16 22 28 27    22 28 27 26    28 27 26 25
#      4 20 14 27    10 14  8 26    16  8  9 25    22  9 15 19
#      3 21  8 26 ->  4 20  9 25 -> 10 14 15 19 -> 16  8 21 13
#      2 15  9 25     3 21 15 19     4 20 21 13    10 14 20  7
#      1  7 13 19     2  1  7 13     3  2  1  7     4  3  2  1
# Sample Input #03

# 2 2 3
# 1 1
# 1 1
# Sample Output #03

# 1 1
# 1 1
# Explanation #03

# All of the elements are the same, so any rotation will repeat the same matrix.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    n , m = len(matrix), len(matrix[0])
    for k in range(min(n,m)//2):
        layer = []
        rotation = r % (2 * (n+m-2-4*k))
        
        for i in range(k, m-k):
            layer.append(matrix[k][i])
            
        for i in range(k+1, n-k-1):
            layer.append(matrix[i][m-k-1])
            
        for i in range(m-k-1, k-1, -1):
            layer.append(matrix[n-k-1][i])
            
        for i in range(n-k-2, k , -1):
            layer.append(matrix[i][k])
            
        l = 0 
        for i in range(k, m-k):
            matrix[k][i] = layer [(l+rotation) % len(layer)]
            l +=1
            
        for i in range(k+1, n-k-1):
            matrix[i][m-k-1] = layer[(l+rotation) % len(layer)]
            l += 1
            
        for i in range(m-k-1, k-1, -1):
            matrix[n-k-1][i] = layer[(l+rotation) % len(layer)]
            l += 1
            
        for i in range(n-k-2, k, -1):
            matrix[i][k] = layer[(l+rotation) % len(layer)]
            l += 1

    for i in matrix:
        print(" ".join(map(str, i)))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
