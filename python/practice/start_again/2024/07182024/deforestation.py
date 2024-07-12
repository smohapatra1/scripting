# #   https://www.hackerrank.com/challenges/deforestation-1/problem?isFullScreen=true

# Alice and Bob are playing a game with a rooted tree. The tree has  vertices and the first node, , is always the root. Here are the basic rules:

# They move in alternating turns, and both players always move optimally.
# During each move, a player removes an edge from the tree, disconnecting one of its leaves or branches. The leaf or branch that was disconnected from the rooted tree is removed from the game.
# The first player to be unable to make a move loses the game.
# Alice always makes the first move.
# For example, the diagram below shows a tree of size , where the root is node : tree-initial.png

# Now, if a player removes the edge between  and , then nodes  and  become disconnected from the root and are removed from the game:

# tree-removed.png

# Given the structure of the tree, determine and print the winner of the game. If Alice wins, print ; otherwise print .

# Input Format

# The first line contains a single integer, , denoting the number of test cases.
# For each test case, the first line contains an integer, , denoting the number of nodes in the tree.
# Each of the  subsequent lines contains  space-separated integers,  and , defining an edge connecting nodes  and .

# Constraints

# Output Format

# For each test case, print the name of the winner (i.e.,  or ) on a new line.

# Sample Input

# 1
# 5
# 1 2
# 3 1
# 3 4
# 4 5
# Sample Output

# Alice
# Explanation

# Test Case 0:

# Alice removes the edge connecting node  to node , effectively trimming nodes  and  from the tree. Now the only remaining edges are  and . Because Bob can't remove both of them, Alice will make the last possible move. Because the last player to move wins, we print  on a new line.

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from operator import xor


#
# Complete the 'deforestation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY tree
#

def deforestation(n, tree):
    # Write your code here
    root = build_tree(n, tree)
    return 'Alice' if grundy(root) else 'Bob'
def build_tree(n, edges):
    neighbors = [set() for _ in range(n+1)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    def get_branch(parent, m ):
        return [get_branch(m, c) for c in neighbors[m] if c !=parent]
    return [get_branch(1, c) for c in neighbors[1]]
def grundy(family):
    return reduce(xor, (1+grundy(branch) for branch in family),0) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        tree = []

        for _ in range(n - 1):
            tree.append(list(map(int, input().rstrip().split())))

        result = deforestation(n, tree)

        fptr.write(result + '\n')

    fptr.close()
