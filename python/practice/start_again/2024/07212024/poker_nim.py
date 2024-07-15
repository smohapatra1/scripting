# #   https://www.hackerrank.com/challenges/poker-nim-1/problem?isFullScreen=true

# Poker Nim is another -player game that's a simple variation on a Nim game. The rules of the games are as follows:

# The game starts with  piles of chips indexed from  to . Each pile  (where ) has  chips.
# The players move in alternating turns. During each move, the current player must perform either of the following actions:

# Remove one or more chips from a single pile.
# Add one or more chips to a single pile.
# At least  chip must be added or removed during each turn.

# To ensure that the game ends in finite time, a player cannot add chips to any pile  more than  times.
# The player who removes the last chip wins the game.
# Given the values of , , and the numbers of chips in each of the  piles, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.

# Input Format

# The first line contains an integer, , denoting the number of test cases.
# Each of the  subsequent lines defines a test case. Each test case is described over the following two lines:

# Two space-separated integers,  (the number of piles) and  (the maximum number of times an individual player can add chips to some pile ), respectively.
#  space-separated integers, , where each  describes the number of chips at pile .
# Constraints

# Output Format

# For each test case, print the name of the winner on a new line (i.e., either  or ).

# Sample Input

# 2
# 2 5
# 1 2
# 3 5
# 2 1 3
# Sample Output

# First
# Second


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pokerNim' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY c
#

def pokerNim(k, c):
    # Write your code here
    res = 0 
    for size in c :
        res ^= size
    return 'First' if res else 'Second' 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        c = list(map(int, input().rstrip().split()))

        result = pokerNim(k, c)

        fptr.write(result + '\n')

    fptr.close()
