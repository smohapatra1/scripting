# #   https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem?isFullScreen=true

# Consider a matrix where each cell contains either a  or a . Any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the following grid, all cells marked X are connected to the cell marked Y.

# XXX
# XYX  
# XXX    
# If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to zero or more cells in the region but is not necessarily directly connected to all the other cells in the region.

# Given an  matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.

# For example, there are two regions in the following  matrix. The larger region at the top left contains  cells. The smaller one at the bottom right contains .

# 110
# 100
# 001
# Function Description

# Complete the connectedCell function in the editor below.

# connectedCell has the following parameter(s):
# - int matrix[n][m]:  represents the  row of the matrix

# Returns
# - int: the area of the largest region

# Input Format

# The first line contains an integer , the number of rows in the matrix.
# The second line contains an integer , the number of columns in the matrix.
# Each of the next  lines contains  space-separated integers .

# Constraints

# Sample Input

# STDIN       Function
# -----       --------
# 4           n = 4
# 4           m = 4
# 1 1 0 0     grid = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
# 0 1 1 0
# 0 0 1 0
# 1 0 0 0
# Sample Output

# 5
# Explanation

# The diagram below depicts two regions of the matrix. Connected regions are filled with X or Y. Zeros are replaced with dots for clarity.

# X X . .
# . X X .
# . . X .
# Y . . .
# The larger region has  cells, marked X.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    def recursive(i, j):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0:
            return 0
        
        # Cell is already being processed, so remove it to avoid false counting in further 
        # recursive executions
        matrix[i][j] = 0
        # Counting current cell 
        size = 1        
        
        size += recursive(i-1, j-1)
        size += recursive(i-1, j)
        size += recursive(i-1, j+1)
        size += recursive(i, j-1)
        size += recursive(i, j+1)
        size += recursive(i+1, j-1)
        size += recursive(i+1, j)
        size += recursive(i+1, j+1)

        return size
    
    # Greedy approach, run for all non zero cells to find the maximum region size    
    max_region_size = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                region_size = recursive(i,j)
                max_region_size = max(max_region_size, region_size)

    return max_region_size 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
