# #   https://www.hackerrank.com/challenges/zero-move-nim/problem?isFullScreen=true

# Nim is a famous game in which two players take turns removing items from  distinct piles. During each turn, a player must remove one or more items from a single, non-empty pile. The winner of the game is whichever player removes the last item from the last non-empty pile.

# John and Kate modified Nim by adding the following rule, which they call a Zero-Move:

# For each non-empty pile, either player can remove  items from that pile and have it count as their move; however, this move can only be performed once per pile by either player. For example, let's say pile  initially has  items in it. If John decides to use a Zero-Move on pile , then neither John nor Kate can perform another Zero-Move on pile ; that said, either player is free to perform a Zero-Move on any other non-empty pile that hasn't had a Zero-Move performed on it yet.

# John and Kate play  games of Zero-Move Nim. Given the number of items in each pile for each game, determine whether or not John can win the game if he always moves first and each player always moves optimally (i.e., never makes a move that causes them to lose if some better, winning move exists). For each game, print W on a new line if John can win; otherwise, print L instead.

# Input Format

# The first line contains an integer, , denoting the number of games. The  subsequent lines describe each game over two lines:

# The first line contains an integer, , denoting the number of heaps.
# The second line contains  space-separated integers describing .
# Constraints

# Subtasks

# For  of the test cases, 
# For  of the test cases, 
# Output Format

# For each game, print W on a new line if John will win; otherwise, print L instead.

# Sample Input 0

# 2
# 2
# 1 2
# 2
# 2 2
# Sample Output 0

# W
# L
# Explanation 0

# John and Kate play the following  games:

# We have two piles,  and . John removes  item from , so . Now that there is only  item in each pile, gameplay can proceed in either of the following ways:

# Kate removes the last object from one pile, then John removes the last object from the other pile.
# Kate uses a Zero-Move on one of the piles, and John uses a Zero-Move on the other pile. Next, Kate must take the last object from one pile, at which point John removes the last object from the other pile.
# Because John always wins in either scenario, we print W on a new line.

# John cannot win this game because the two piles are of equal size and Kate has an opportunity to counter any move he makes by performing the same action. Consider the following scenarios:

# If John uses a Zero-Move on one pile, Kate can use a Zero-Move on the other pile (meaning the piles still have the same configuration after both players move).
# If John removes one element from a pile, Kate can remove one element from the other pile so that both remaining piles contain one element when John takes his next turn. He would then be forced to empty one of the piles, leaving Kate to make the winning move by emptying the last pile.
# If John removes both elements from one of the piles, Kate can remove both elements from the other pile and win the game.
# Because John always loses this game, we print L on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'zeroMoveNim' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def zeroMoveNim(p):
    # Write your code here
    p=[i-1+2*(i%2) for i in p]
    return 'W' if reduce((lambda x,y:x^y),p) else 'L'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        # p_count = int(input().strip())

        p = list(map(int, input().rstrip().split()))

        result = zeroMoveNim(p)

        fptr.write(str(result) + '\n')

    fptr.close()
