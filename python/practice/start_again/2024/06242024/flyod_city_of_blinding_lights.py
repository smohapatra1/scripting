# #   https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem?isFullScreen=true

# Given a directed weighted graph where weight indicates distance, for each query, determine the length of the shortest path between nodes. There may be many queries, so efficiency counts.

# For example, your graph consists of  nodes as in the following:

# image

# A few queries are from node  to node , node  to node , and node  to node .


# There are two paths from  to :

#  at a distance of 
#  at a distance of 
# In this case we choose path .
# There is no path from  to , so we return .

# There is one path from  to :

#  at a distance of .
# Input Format

# The first line has two integers  and , the number of nodes and the number of edges in the graph.
# Each of the next  lines contains three space-separated integers   and , the two nodes between which the directed edge  exists, and , the length of the edge.
# The next line contains a single integer , the number of queries.
# Each of the next  lines contains two space-separated integers  and , denoting the start and end nodes for traversal.

# Constraints






# The distance from a node to itself is always  and it is always reachable from itself.

# If there are edges between the same pair of nodes with different weights, the last one (most recent) is to be considered as the only edge between them.

# Output Format

# Print  lines, each containing a single integer specifying the shortest distance for the query.

# If the destination node is not reachable, return .

# Sample Input

# STDIN   Function
# -----   --------
# 4 5     n = 4, m = 5
# 1 2 5   u = 1, v = 2, w = 5
# 1 4 24  u = 1, v =4, w = 24 ...
# 2 4 6
# 3 4 4
# 3 2 7
# 3       q = 3
# 1 2     query 0: from 1 to 2
# 3 1     query 1: from 3 to 1
# 1 4     query 2: from 1 to 4
# Sample Output

# 5
# -1
# 11
# Explanation

# The graph given in the test case is:

# image

# The shortest paths for the 3 queries are :

# : The direct path is shortest with weight 5
# : There is no way of reaching node 1 from node 3
# : The indirect path is shortest with weight (5+6) = 11 units. The direct path is longer with 24 units length.


#!/bin/python3

import math
import os
import random
import re
import sys


from sys import stdin
from collections import defaultdict
import heapq

n, m = (int(x) for x in stdin.readline().split())
adj = defaultdict(dict)
for mi in range(m):
    x, y, r = (int(z) for z in stdin.readline().split())
    adj[x][y]=r
q = int(stdin.readline().strip())
dists = {}
heap = {}
for ni in range(1,n+1):
    dists[ni]= {}
    heap[ni]=[(0,ni)]
    
for qi in range(q):
    a, b = (int(x) for x in stdin.readline().split())
    while b not in dists[a]:
        if not heap[a]:
            dists[a][b] = -1
            break
        dv, v = heapq.heappop(heap[a])
        if v not in dists[a]:
            dists[a][v]=dv
            for y, dy in adj[v].items():
                heapq.heappush(heap[a], (dv + dy, y))
        
    print(dists[a][b])

# if __name__ == '__main__':
#     road_nodes, road_edges = map(int, input().rstrip().split())

#     road_from = [0] * road_edges
#     road_to = [0] * road_edges
#     road_weight = [0] * road_edges

#     for i in range(road_edges):
#         road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

#     q = int(input().strip())

#     for q_itr in range(q):
#         first_multiple_input = input().rstrip().split()

#         x = int(first_multiple_input[0])

#         y = int(first_multiple_input[1])
