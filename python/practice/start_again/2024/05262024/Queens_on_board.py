# #   https://www.hackerrank.com/challenges/queens-on-board/problem?isFullScreen=true

# Queens on Board

# You have an N * M chessboard on which some squares are blocked out. In how many ways can you place one or more queens on the board, such that, no two queens attack each other? Two queens attack each other, if one can reach the other by moving horizontally, vertically, or diagonally without passing over any blocked square. At most one queen can be placed on a square. A queen cannot be placed on a blocked square.

# Input Format

# The first line contains the number of test cases T. T test cases follow. Each test case contains integers N and M on the first line. The following N lines contain M characters each, and represent a board. A '#' represents a blocked square and a '.' represents an unblocked square.

# Constraints

# 1 <= T <= 100
# 1 <= N <= 50
# 1 <= M <= 5

# Output Format

# Output T lines containing the required answer for each test case. As the answers can be really large, output them modulo 109+7.

# Sample Input

# 4  
# 3 3  
# ...  
# ...  
# ...  
# 3 3  
# .#.  
# .#.  
# ...  
# 2 4  
# .#..  
# ....  
# 1 1  
# #
# Sample Output

# 17  
# 18  
# 14  
# 0 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensBoard' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY board as parameter.
#


def memoize(func):
    pool = {}
    def wrapper(*arg):
        if arg not in pool:
            pool[arg] = func(*arg)
        return pool[arg]
    return wrapper

mod = 1000000007

for case in range(int(input())):
    Y,X = map(int,input().split())
    mx = [int(''.join('0' if c =='.' else '1' for c in input().rstrip()), 2) for i in range(Y)]
    full = (1<<X)-1

    def is_wall(x,y):
        return mx[y] & (1<<x) != 0 if 0<=x<X and 0<=y<Y else True

    def get_free(mx):
        y = 0
        while y<Y and mx[y] == full:
            y+=1

        if y==Y: return (None,None)
        free = 0
        while mx[y] & (1<<free) != 0:
            free += 1
        if free >= X: return (None,None)
        return (free,y)

    def place_queen(x,y,mx):
        nmx = list(mx)
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx == 0 and dy == 0: continue
                cx,cy = x,y
                while not is_wall(cx,cy):
                    nmx[cy] |= (1<<cx)
                    cx,cy = cx+dx,cy+dy
        return tuple(nmx)
        
    @memoize
    def rec(mx):
        free_x,free_y = get_free(mx)
        if free_x == None: return 0
        #ignore free place
        imx = list(mx)
        imx[free_y] |= 1<<free_x
        ans = rec(tuple(imx))
        #place queen to free
        nmx = place_queen(free_x,free_y,mx)
        ans += 1
        free_x,free_y = get_free(nmx)
        if free_x != None:
            ans += rec(nmx)
        return ans % mod

    print(rec(tuple(mx)))
    
# def queensBoard(board):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         board = []

#         for _ in range(n):
#             board_item = input()
#             board.append(board_item)

#         result = queensBoard(board)

#         fptr.write(str(result) + '\n')

#     fptr.close()
