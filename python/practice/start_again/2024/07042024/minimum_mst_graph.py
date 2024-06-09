# #   https://www.hackerrank.com/challenges/minimum-mst-graph/problem?isFullScreen=true

# Allison loves graph theory and just started learning about Minimum Spanning Trees(MST). She has three integers, , , and , and uses them to construct a graph with the following properties:

# The graph has  nodes and  undirected edges where each edge has a positive integer length.
# No edge may directly connect a node to itself, and each pair of nodes can only be directly connected by at most one edge.
# The graph is connected, meaning each node is reachable from any other node.
# The value of the minimum spanning tree is . Value of the MST is the sum of all the lengths of all edges of which are part of the tree.
# The sum of the lengths of all edges is as small as possible.
# For example, let's say ,  and . We need to construct a graph with  nodes and  edges. The value of minimum spanning tree must be . The diagram belows shows a way to construct such a graph while keeping the lengths of all edges is as small as possible:

# image

# Here the sum of lengths of all edges is .

# Given , , and  for  graphs satisfying the conditions above, find and print the minimum sum of the lengths of all the edges in each graph on a new line.

# Note: It is guaranteed that, for all given combinations of , , and , we can construct a valid graph.

# Input Format

# The first line contains an integer, , denoting the number of graphs.
# Each of the  subsequent lines contains three space-separated integers describing the respective values of  (the number of nodes in the graph),  (the number of edges in the graph), and  (the value of the MST graph).

# Constraints

# For  of the maximum score:

    
    
    
    
# For  of the maximum score:

    
    
    
    
# For  of the maximum score:

    
    
    
    
# For  of the maximum score:

    
    
    
    
# Output Format

# For each graph, print an integer on a new line denoting the minimum sum of the lengths of all edges in a graph satisfying the given conditions.

# Sample Input

# 2
# 4 5 4
# 4 3 6
# Sample Output

# 7
# 6
# Explanation

# Graph :
# The answer for this sample is already explained the problem statement.

# Graph :
# We must construct a graph with  nodes,  edges, and an MST value of . Recall that a connected graph with  nodes and  edges is already a tree, so the MST will contain all  edges and the total length of all the edges of the graph will be equal to the value of the minimum spanning tree. So the answer is .


#!/bin/python3

import math
import os
import random
import re
import sys

g = int(input().strip())
for a0 in range(g):
    n,m,s = input().strip().split(' ')
    n,m,s = [int(n),int(m),int(s)]
    
    if m <= (n - 1) * (n - 2) // 2 + 1:
        print(m + s - n + 1)
    else:
        s -= n - 1
        e = m - (n - 1) * (n - 2) // 2
        mnc = (s + n - 2) // (n - 1)
        ans = 1e42
        s -= mnc
        for A in [0, s // (n - 2), s // (n - 2) - 1]:
            for B in [0, n - 3, (s - A * (n - 2)) % (n - 2)]:
                x = A * (n - 2) + B
                if 0 <= x <= s:
                    ans = min(ans, (s - x + mnc) * e + (n - 1) * (n - 2) // 2 * A + B * (B - 1) // 2 + B * (n - B - 1))

        print(ans + m)
        

# if __name__ == '__main__':
#     g = int(input())

#     for g_itr in range(g):
#         nms = input().split()

#         n = int(nms[0])

#         m = int(nms[1])

#         s = int(nms[2])

#         # Write Your Code Here
