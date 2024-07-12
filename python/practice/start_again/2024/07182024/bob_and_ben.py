# #   https://www.hackerrank.com/challenges/bob-and-ben/problem?isFullScreen=true

# Bob and Ben are playing a game with forests! The game's rules are as follows:

# The game starts with a forest of  trees.
# Bob always moves first and they take alternating turns. The first player with no available move loses the game.
# During each move, the player removes one node. If the node is not a leaf, then the whole tree vanishes; otherwise, the rest of the tree remains in the forest. We define a leaf to be a node with exactly  connected edge.
# Both players play optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists.
# We define each tree  in the -tree forest as follows:

# Tree  is defined by two integers,  (the number of nodes in the tree) and  (a constant).
# Its nodes are numbered sequentially from  to .
# Its edges are numbered sequentially from  to , and each edge  connects node  to node .
# Given the values of  and  for each tree in the forest, can you determine who will win the game?

# Input Format

# The first line contains an integer, , denoting the number of games. The subsequent lines describe each game in the following format:

# The first line contains an integer, , denoting the number of trees in the forest.
# Each of the  subsequent lines contains two space-separated integers describing the respective values of  and  for tree .
# Constraints

# The sum of  over all games is at most .
# Subtasks

# For  of the maximum score:

# The sum of  over all games is at most .
# For  of the maximum score:

# Output Format

# For each game, print the name of the winner on a new line (i.e., BOB or BEN).

# Sample Input

# 2
# 2
# 1 2
# 1 3
# 1
# 3 2
# Sample Output

# BEN
# BOB
# Explanation

# Bob and Ben play the following two games:

# The forest consists of  trees containing one node each, and each tree has no edges as  and  are both  (so both trees have  edges). The sequence of moves is as follows:
# image
# We then print the name of the winner, BEN, on a new line.
# The forest consists of  tree containing three nodes. We find the  edges like so:

# Edge  connects node  to node .
# Edge  connects node  to node .
# The game then plays out as follows:
# image
# We then print the name of the winner, BOB, on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bobAndBen' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY trees as parameter.
#

def GrudyNumbers(nodes):
    if nodes == 0 or nodes == 2:
        return 0
    else:
        return ((nodes -1)%2 +1)

def bobAndBen(trees):
    # Write your code here
    GrudyNumers = []
    for i in range(len(trees)):
        GrudyNumers.append(GrudyNumbers(trees[i][0]))
    res = GrudyNumers[0]
    # print (GrudyNumbers)
    if (len(GrudyNumers)-1) > 1:
        for j in range(1, len(GrudyNumers)):
            res ^=GrudyNumers[j]
    elif ((len(GrudyNumers)-1) ==1 ):
        res = res^GrudyNumers[1]
    if res != 0:
        return 'BOB'
    else:
        return 'BEN'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        trees = []

        for _ in range(n):
            trees.append(list(map(int, input().rstrip().split())))

        result = bobAndBen(trees)

        fptr.write(result + '\n')

    fptr.close()
