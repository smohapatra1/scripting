# #   https://www.hackerrank.com/challenges/misere-nim-1/problem?isFullScreen=true

# Two people are playing game of Misère Nim. The basic rules for this game are as follows:

# The game starts with  piles of stones indexed from  to . Each pile  (where ) has  stones.
# The players move in alternating turns. During each move, the current player must remove one or more stones from a single pile.
# The player who removes the last stone loses the game.
# Given the value of  and the number of stones in each pile, determine whether the person who wins the game is the first or second person to move. If the first player to move wins, print First on a new line; otherwise, print Second. Assume both players move optimally.

# Example

# In this case, player 1 picks a pile, player 2 picks a pile and player 1 has to choose the last pile. Player 2 wins so return Second.


# There is no permutation of optimal moves where player 2 wins. For example, player 1 chooses the first pile. If player 2 chooses 1 from another pile, player 1 will choose the pile with 2 left. If player 2 chooses a pile of 2, player 1 chooses 1 from the remaining pile leaving the last stone for player 2. Return First.

# Function Description

# Complete the misereNim function in the editor below.

# misereNim has the following parameters:

# int s[n]: the number of stones in each pile
# Returns

# string: either First or Second
# Input Format

# The first line contains an integer, , the number of test cases.
# Each test case is described over two lines:

# An integer, , the number of piles.
#  space-separated integers, , that describe the number of stones at pile .
# Constraints

# Sample Input

# STDIN   Function
# -----   --------
# 2       T = 2
# 2       s[] size n = 2
# 1 1     s = [1, 1]
# 3       s[] size n = 3
# 2 1 3   s = [2, 1, 3]
# Sample Output

# First
# Second
# Explanation

# In the first testcase, the first player removes 1 stone from the first pile and then the second player has no moves other than removing the only stone in the second pile. So first wins.

# In the second testcase, the series of moves can be depicted as:

# image

# In every possible move of first player we see that the last stone is picked by him, so second player wins.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

r = ['First', 'Second']
for i in range(int(input())):
    input()
    c, a = 1, list(map(int, input().split()))
    s = a[0]
    
    for j in range(1,len(a)): s ^= a[j]
    for j in a:
        if j > 1: c = 0
           
    print(r[s == c])
    

# def misereNim(s):
#     # Write your code here
        

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         s = list(map(int, input().rstrip().split()))

#         result = misereNim(s)

#         fptr.write(result + '\n')

#     fptr.close()
