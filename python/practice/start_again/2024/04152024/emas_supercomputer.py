# #   https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true

# Ema built a quantum computer! Help her test its capabilities by solving the problem below.

# Given a grid of size , each cell in the grid is either  or .

# A valid plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.

# In the diagram below, the blue pluses are valid and the orange ones are not valid. pluseses.png

# Find the two largest valid pluses that can be drawn on  cells in the grid, and return an integer denoting the maximum product of their areas. In the above diagrams, our largest pluses have areas of  and . The product of their areas is .

# Note: The two pluses cannot overlap, and the product of their areas should be maximal.

# Function Description

# Complete the twoPluses function in the editor below. It should return an integer that represents the area of the two largest pluses.

# twoPluses has the following parameter(s):

# grid: an array of strings where each string represents a row and each character of the string represents a column of that row
# Input Format

# The first line contains two space-separated integers,  and .
# Each of the next  lines contains a string of  characters where each character is either G () or B (). These strings represent the rows of the grid. If the  character in the  line is G, then  is a  cell. Otherwise it's a  cell.

# Constraints



# Output Format

# Find  pluses that can be drawn on  cells of the grid, and return an integer denoting the maximum product of their areas.

# Sample Input 0

# 5 6
# GGGGGG
# GBBBGB
# GGGGGG
# GGBBGB
# GGGGGG
# Sample Output 0

# 5
# Sample Input 1

# 6 6
# BGBBGB
# GGGGGG
# BGBBGB
# GGGGGG
# BGBBGB
# BGBBGB
# Sample Output 1

# 25
# Explanation

# Here are two possible solutions for Sample 0 (left) and Sample 1 (right): plusss.png

# Explanation Key:

# Green:  cell
# Red:  cell
# Blue: possible .
# For the explanation below, we will refer to a plus of length  as .

# Sample 0
# There is enough good space to color one  plus and one  plus. , and . The product of their areas is .

# Sample 1
# There is enough good space to color two  pluses. . The product of the areas of our two  pluses is .


#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    h, w = len(grid), len(grid[0])
    plus = []
    isGood = lambda r, c: grid[r][c] == 'G'
    for step in range(1, min(h,w) //2 + min(h, w) % 2 ):
        for r in range(step, h-step):
            for c in range(step, w-step):
                if isGood(r, c):
                    s1 = {(r2, c) for r2 in range(r-1, r-step-1, -1) if isGood(r2, c)}
                    s2 = {(r2, c) for r2 in range(r+1, r+step+1, +1) if isGood(r2, c)}
                    s3 = {(r, c2) for c2 in range(c-1, c-step-1, -1) if isGood(r, c2)}
                    s4 = {(r, c2) for c2 in range(c+1, c+step+1, +1) if isGood(r, c2)}
                    if len(s1) == step and len(s2) == step and len(s3) == step and len(s4) == step:
                        plus.append((4*step+1, {(r,c)}|s1|s2|s3|s4))
    if not plus:
        return 1
    if len(plus) == 1:
        return plus.pop()[0]
    combs = [s1 * s2 for (s1, a ), (s2, b ) in combinations (plus, 2) if a.isdisjoint(b)]
    return max(combs) if combs else plus.pop()[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
