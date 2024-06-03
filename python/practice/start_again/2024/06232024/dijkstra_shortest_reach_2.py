# #   https://www.hackerrank.com/challenges/dijkstrashortreach/problem?isFullScreen=true

# Given an undirected graph and a starting node, determine the lengths of the shortest paths from the starting node to all other nodes in the graph. If a node is unreachable, its distance is -1. Nodes will be numbered consecutively from  to , and edges will have varying distances or lengths.

# For example, consider the following graph of 5 nodes:

# Begin	End	Weight
# 1	2	5
# 2	3	6
# 3	4	2
# 1	3	15
# image
# Starting at node , the shortest path to  is direct and distance . Going from  to , there are two paths:  at a distance of  or  at a distance of . Choose the shortest path, . From  to , choose the shortest path through  and extend it:  for a distance of  There is no route to node , so the distance is .

# The distances to all nodes in increasing node order, omitting the starting node, are 5 11 13 -1.

# Function Description

# Complete the shortestReach function in the editor below. It should return an array of integers that represent the shortest distance to each node from the start node in ascending order of node number.

# shortestReach has the following parameter(s):

# n: the number of nodes in the graph
# edges: a 2D array of integers where each  consists of three integers that represent the start and end nodes of an edge, followed by its length
# s: the start node number
# Input Format

# The first line contains , the number of test cases.

# Each test case is as follows:
# - The first line contains two space-separated integers  and , the number of nodes and edges in the graph.
# - Each of the next  lines contains three space-separated integers , , and , the beginning and ending nodes of an edge, and the length of the edge.
# - The last line of each test case has an integer , denoting the starting position.

# Constraints






# If there are edges between the same pair of nodes with different weights, they are to be considered as is, like multiple edges.

# Output Format

# For each of the  test cases, print a single line consisting  space separated integers denoting the shortest distance to the  nodes from starting position  in increasing order of their labels, excluding .

# For unreachable nodes, print .

# Sample Input

# 1
# 4 4
# 1 2 24
# 1 4 20
# 3 1 3
# 4 3 12
# 1
# Sample Output

# 24 3 15
# Explanation

# The graph given in the test case is shown as :

# image
# * The lines are weighted edges where weight denotes the length of the edge.

# The shortest paths followed for the three nodes 2, 3 and 4 are as follows :

# 1/S->2 - Shortest Path Value : 

# 1/S->3 - Shortest Path Value : 

# 1/S->3->4 - Shortest Path Value : 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

from collections import OrderedDict
from collections import defaultdict


class Graph:

    def __init__(self):
        self.neighbors = defaultdict(set)
        self.vertices = list()

    def add_edge(self, start, end, distance):
        self.neighbors[start].add((end, distance))
        self.neighbors[end].add((start, distance))


def dijkstra(graph, start):
    # value to represent infinity
    infinity = object()
    # distances
    distances = OrderedDict()
    for vertex in graph.vertices:
        distances[vertex] = infinity
    distances[start] = 0

    # XXX: create trampoline
    trampoline = list()

    def compute(current):
        # XXX: global variables are used
        for neighbor, distance in graph.neighbors[current]:
            # replace distance with the shortest distance
            new = distances[current] + distance
            if (distances[neighbor] is infinity or distances[neighbor] > new):  # noqa
                distances[neighbor] = new
                trampoline.append(neighbor)

    # boostrap
    trampoline.append(start)
    # ignite trampoline
    while trampoline:
        vertex = trampoline.pop(0)
        compute(vertex)

    # remove start node
    distances = list(distances.values())
    distances.pop(start - 1)
    return map(lambda x: -1 if x is infinity else x, distances)


T = int(input())


for _ in range(T):
    graph = Graph()

    N, M = map(int, input().split())
    for name in range(1, N + 1):
        graph.vertices.append(name)

    for _ in range(M):
        start, end, distance = map(int, input().split())
        graph.add_edge(start, end, distance)

    S = int(input())
    print(' '.join(map(str, dijkstra(graph, S))))

# def shortestReach(n, edges, s):
#     # Write your code here
#     vertices = [[] for _ in range(n)]
#     for u, v, w in edges:
#         vertices[u - 1].append((v - 1, w))
#         vertices[v - 1].append((u - 1, w))
#     for i, v in enumerate(vertices):
#         vertices[i] = sorted(v, key=lambda x : x[1])
#     dist = [1E9 for _ in range(n)]
#     s = s - 1
#     dist[s] = 0
#     que = [(s, 0)]
#     while que:
#         u, d = que.pop(0)
#         if d > dist[u]:
#             continue
#         for v, w in vertices[u]:
#             val = w + dist[u]
#             if val < dist[v]:
#                 dist[v] = val
#                 que.append((v, val))
#     dist.pop(s)
#     for i, d in enumerate(dist):
#         if d > 1E9 - 1:
#             dist[i] = -1
#     return dist

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         edges = []

#         for _ in range(m):
#             edges.append(list(map(int, input().rstrip().split())))

#         s = int(input().strip())

#         result = shortestReach(n, edges, s)

#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')

#     fptr.close()


