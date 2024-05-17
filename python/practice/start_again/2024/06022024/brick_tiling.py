# #   https://www.hackerrank.com/challenges/brick-tiling/problem?isFullScreen=true

# You are given a grid having N rows and M columns. A grid square can either be blocked or empty. Blocked squares are represented by a '#' and empty squares are represented by '.'. Find the number of ways to tile the grid using L shaped bricks. A L brick has one side of length three units while other of length 2 units. All empty squares in the grid should be covered by exactly one of the L shaped tiles, and blocked squares should not be covered by any tile. The bricks can be used in any orientation (they can be rotated or flipped).

# Input Format

# The first line contains the number of test cases T. T test cases follow. Each test case contains N and M on the first line, followed by N lines describing each row of the grid.

# Constraints

# 1 <= T <= 50
# 1 <= N <= 20
# 1 <= M <= 8
# Each grid square will be either '.' or '#'.

# Output Format

# Output the number of ways to tile the grid. Output each answer modulo 1000000007.

# Sample Input

# 3  
# 2 4  
# ....  
# ....  
# 3 3  
# ...  
# .#.  
# ...  
# 2 2  
# ##  
# ##
# Sample Output

# 2  
# 4  
# 1
# Explanation

# NOTE:
# If all points in the grid are blocked the number of ways is 1, as in the last sample testcase.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'brickTiling' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def memoize(func):
    pool = {}
    def wrapper(*arg):
        if arg not in pool:
            pool[arg] = func(*arg)
        return pool[arg]
    return wrapper

mod = 1000000007
shapes = (\
    ((1,0),(2,0),(2,1)),\
    ((0,1),(0,2),(-1,2)),\
    ((0,1),(1,1),(2,1)),\
    ((1,0),(0,1),(0,2)),\
    ((0,1),(-1,1),(-2,1)),\
    ((0,1),(0,2),(1,2)),\
    ((1,0),(2,0),(0,1)),\
    ((1,0),(1,1),(1,2)))

for case in range(int(input())):
    Y,X = map(int,input().split())
    mx = [int(''.join('0' if c =='.' else '1' for c in input().rstrip()), 2) for i in range(Y)]
    mx = mx + 3*[0]
    full = (1<<X)-1

    @memoize
    def rec(y,first,second,third):
        if y==Y:
            return 1 if first == second and second == third and third == 0 else 0
        if first == full:
            return rec(y+1,second,third,mx[y+3])

        def can_fit(rows,shape,x_offset):
            res = rows[:]
            for x,y in shape:
                x += x_offset
                if x < 0 or x >= X or y < 0 or y >= Y:
                    return None
                if res[y] & (1<<x) != 0:
                    return None
                res[y] |= (1<<x)
            return res

        free = 0
        while (first & (1<<free)) != 0:
            free += 1
        rows = [first | (1<<free),second,third]
        ans = 0
        for shape in shapes:
            nrows = can_fit(rows,shape,free)
            if nrows != None:
                ans = (ans + rec(y, *nrows)) % mod
        return ans

    print(rec(0,mx[0],mx[1],mx[2]))
    

# def brickTiling(grid):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         grid = []

#         for _ in range(n):
#             grid_item = input()
#             grid.append(grid_item)

#         result = brickTiling(grid)

#         fptr.write(str(result) + '\n')

#     fptr.close()
