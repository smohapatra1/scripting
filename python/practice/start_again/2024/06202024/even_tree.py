# #   https://www.hackerrank.com/challenges/even-tree/problem?isFullScreen=true

# You are given a tree (a simple connected graph with no cycles).

# Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of nodes.

# As an example, the following tree with  nodes can be cut at most  time to create an even forest.

# image

# Function Description

# Complete the evenForest function in the editor below. It should return an integer as described.

# evenForest has the following parameter(s):

# t_nodes: the number of nodes in the tree
# t_edges: the number of undirected edges in the tree
# t_from: start nodes for each edge
# t_to: end nodes for each edge, (Match by index to t_from.)
# Input Format

# The first line of input contains two integers  and , the number of nodes and edges.
# The next  lines contain two integers  and  which specify nodes connected by an edge of the tree. The root of the tree is node .

# Constraints

# Note: The tree in the input will be such that it can always be decomposed into components containing an even number of nodes.  is the set of positive even integers.

# Output Format

# Print the number of removed edges.

# Sample Input 1

# CopyDownload
# Undirected Graph: t
# 2
# 1
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

 
# 10 9
# 2 1
# 3 1
# 4 3
# 5 2
# 6 1
# 7 2
# 8 6
# 9 8
# 10 8
# Sample Output 1

# 2
# Explanation 1

# Remove edges  and  to get the desired result.


# image image

# No more edges can be removed.


#!/bin/python3

import math
import os
import random
import re
import sys


def read_tree(N):
    tree = dict()
    while N:
        t, f = [int(i) for i in (cin.readline().split(' ', 1))]
        if f not in tree:
            tree[f] = [t]
        else:
            tree[f].append(t)
        N -= 1
    return tree


def num_to_remove(tree, node, cnt):
    if node not in tree:
        return 1
    sum = 1
    for i in tree[node]:
        ns = num_to_remove(tree, i, cnt)
        if not ns & 1:
            cnt[0] += 1
        else:
            sum += ns
    return sum


if __name__ == "__main__":
    cin = None

    if len(sys.argv) > 1:
        cin = open(sys.argv[1])
    else:
        cin = sys.stdin

    N, M = [int(i) for i in (cin.readline().split(' ', 1))]

    cnt = [0]
    num_to_remove(read_tree(M), 1, cnt)
    print(cnt[0])

    if cin is not sys.stdin:
        cin.close()
    pass

# # Complete the evenForest function below.
# def evenForest(t_nodes, t_edges, t_from, t_to):

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t_nodes, t_edges = map(int, input().rstrip().split())

#     t_from = [0] * t_edges
#     t_to = [0] * t_edges

#     for i in range(t_edges):
#         t_from[i], t_to[i] = map(int, input().rstrip().split())

#     res = evenForest(t_nodes, t_edges, t_from, t_to)

#     fptr.write(str(res) + '\n')

#     fptr.close()
