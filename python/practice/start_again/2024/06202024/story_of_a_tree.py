# #   https://www.hackerrank.com/challenges/the-story-of-a-tree/problem?isFullScreen=true

# One day Bob drew a tree, , with  nodes and  edges on a piece of paper. He soon discovered that parent of a node depends on the root of the tree. The following images shows an example of that:

# image

# Learning the fact, Bob invented an exciting new game and decided to play it with Alice. The rules of the game is described below:

# Bob picks a random node to be the tree's root and keeps the identity of the chosen node a secret from Alice. Each node has an equal probability of being picked as the root.
# Alice then makes a list of  guesses, where each guess is in the form u v and means Alice guesses that  is true. It's guaranteed that an undirected edge connecting  and  exists in the tree.
# For each correct guess, Alice earns one point. Alice wins the game if she earns at least  points (i.e., at least  of her guesses were true).
# Alice and Bob play  games. Given the tree, Alice's guesses, and the value of  for each game, find the probability that Alice will win the game and print it on a new line as a reduced fraction in the format p/q.

# Input Format

# The first line contains an integer, , denoting the number of different games. The subsequent lines describe each game in the following format:

# The first line contains an integer, , denoting the number of nodes in the tree.
# The  subsequent lines contain two space-separated integers,  and , defining an undirected edge between nodes  and .
# The next line contains two space-separated integers describing the respective values of  (the number of guesses) and  (the minimum score needed to win).
# Each of the  subsequent lines contains two space-separated integers,  and , indicating Alice guesses .
# Constraints

# The sum of  over all test cases won't exceed .
# No two guesses will be identical.
# Scoring

# For  of the maximum score, .
# For  of the maximum score, .
# Output Format

# Print the probability as a reduced fraction in the format p/q.

# Note: Print 0/1 if the probability is  and print 1/1 if the probability is .

# Sample Input 0

# 2
# 4
# 1 2
# 1 3
# 3 4
# 2 2
# 1 2
# 3 4
# 3
# 1 2
# 1 3
# 2 2
# 1 2
# 1 3
# Sample Output 0

# 1/2
# 1/3
# Explanation 0

# Alice and Bob play the following  games:

# Alice makes two guesses,  and , meaning she guessed that  and . To win the game, at least  of her guesses must be true.

# In the diagrams below, you can see that at least  guesses are true if the root of the tree is either node  or :

# image

# There are  nodes in total and the probability of picking node  or  as the root is , which reduces to .

# In this game, Alice only wins if node  is the root of the tree. There are  nodes in total, and the probability of picking node  as the root is .



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'storyOfATree' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY guesses
#

from fractions import Fraction
adj = []
guess = set()
visit = []
np = []
base = 0

def rec(node, point):
    global base
    visit[node] = True
    np[node] = point
    for a in adj[node]:
        if visit[a]: continue
        positive = (node, a) in guess
        negative = (a, node) in guess
        if positive and negative:
            base = base + 1
            rec(a, point)
        elif positive:
            base = base + 1
            rec(a, point - 1)
        elif negative:
            rec(a, point + 1)
        else:
            rec(a, point)

for q in range(int(input())):
    n = int(input())
    adj = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = input().split()
        u, v = [int(u) - 1, int(v) - 1]
        adj[u].append(v)
        adj[v].append(u)

    g, k = input().split()
    g, k = [int(g), int(k)]

    guess = set()
    for i in range(g):
        u, v = input().split()
        guess.add((int(u) - 1, int(v) - 1))

    visit = [False] * n
    np = [0] * n
    base = 0
    rec(0, 0)

    count = 0
    for p in np:
        if p + base >= k:
            count = count + 1

    if count == 0:
        print("0/1")
    elif count == n:
        print("1/1")
    else:
        print(Fraction(count, n))
        

# def storyOfATree(n, edges, k, guesses):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         edges = []

#         for _ in range(n - 1):
#             edges.append(list(map(int, input().rstrip().split())))

#         first_multiple_input = input().rstrip().split()

#         g = int(first_multiple_input[0])

#         k = int(first_multiple_input[1])

#         guesses = []

#         for _ in range(q):
#             guesses.append(list(map(int, input().rstrip().split())))

#         result = storyOfATree(n, edges, k, guesses)

#         fptr.write(result + '\n')

#     fptr.close()
