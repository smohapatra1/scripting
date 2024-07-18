# #   https://www.hackerrank.com/challenges/benders-play/problem?isFullScreen=true

# General Iroh and Commandant Bumi are heading to the Republic City to stop a rebellion. But it's quite a long travel, so in the meantime they have started discussing about possible attacking plans. Right now, they're arguing about best ways for moving soldiers during the battle. Tired of not getting a final and concise strategy, Iroh proposed a particularly original idea.

# Iroh:

# Bumi, look at this map: here we have all possible locations in the battle field soldiers can occupy. I know a game which can give us some ideas.
# Bumi:

# A game? How will a game help us here?
# Iroh:

# It's pretty simple, we know which location is connected to each one, and also, that all those paths between locations are one-way (it's too dangerous to have two ways paths), so we place some soldiers at random initial locations, take turns, and in each turn, we try to make a valid move with one soldier from one location to another. Eventually, we won't be able to move any man so, the first one which is not able to perform any valid move, loses. One important thing is, at some moment, we may have some men at the same field location.
# Bumi:

# Are you sure we are gonna end this? We have so many locations and paths... don't know, soldiers could be moving in circles for ever.
# Iroh:

# Take it easy man, those paths were built by the best architects I've ever known, so there is no way that could happen.
# Bumi:

# Well, I still don't get how does this help us.
# Iroh:

# Me neither, but greatest generals from the Earth Kingdom created their strategies from this game, so, who knows?
# Bumi:

# Ok, I'm in. Who plays first?
# Iroh:

# You go first my friend. Just make sure you always do your best, because I will show no mercy to you :).
# Input Format

# First line in the input contains two integers N and M, describing the number of locations and paths between them, respectively. M lines follow, each one with two integers u and v, denoting a one-way path from u to v.
# Then comes a line with a single integer Q, denoting how many times Bumi and Iroh played the game over the given field. Q queries follow each one with two lines, first one with a single integer K, the number of soldiers in the field; and second one with K integers b_i separated by space, each one denoting the initial location of some soldier.

# Constraints

# 1 < N <= 105
# 1 <= M <= 106
# 1 <= u, v, b_i <= N
# 1 <= K <= 102
# 1 <= Q <= 105

# Output Format

# Output Q lines, each one saying Bumi if Bumi should be the winner of the corresponding game or Iroh otherwise.
# Remember that, being both top strategy masters, they will always perform the best possible move each turn.

# Sample Input

# 10 10
# 1 10
# 3 10
# 7 8
# 6 8
# 7 4
# 9 4
# 7 6
# 5 8
# 1 8
# 2 8
# 5
# 4
# 10 7 6 4
# 3
# 1 9 4
# 3
# 8 3 5
# 3
# 4 9 7
# 3
# 7 9 10
# Sample Output

# Bumi
# Iroh
# Iroh
# Bumi
# Bumi

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bendersPlay' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY paths
#  3. INTEGER_ARRAY query
#

from collections import defaultdict
from functools import reduce
from operator import xor
n, m = map(int, input().split())
def mex(s):
    return next(i for i in range(n) if i not in s)
#visit nodes via backward topological sort
childs = defaultdict(set)
parents = defaultdict(set)
leaves = set(range(1, n + 1))
childnum = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    leaves.discard(u)
    childs[u].add(v)
    childnum[u] += 1
    parents[v].add(u)
gnum = [0] * (n + 1)
while leaves:
    curr = leaves.pop()
    gnum[curr] = mex(set(map(gnum.__getitem__, childs[curr])))
    for p in parents[curr]:
        if childnum[p] == 1:
            leaves.add(p)
        else:
            childnum[p] -= 1
res = []
for _ in range(int(input())):
    input()
    res.append("Bumi" if reduce(xor, map(gnum.__getitem__, map(int, input().split())), 0) else "Iroh")
print("\n".join(res))


# def bendersPlay(n, paths, query):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     paths = []

#     for _ in range(m):
#         paths.append(list(map(int, input().rstrip().split())))

#     q = int(input().strip())

#     for q_itr in range(q):
#         query_count = int(input().strip())

#         query = list(map(int, input().rstrip().split()))

#         result = bendersPlay(n, paths, query)

#         fptr.write(result + '\n')

#     fptr.close()
