# #   https://www.hackerrank.com/challenges/primsmstsub/problem?isFullScreen=true

# Given a graph which consists of several edges connecting its nodes, find a subgraph of the given graph with the following properties:

# The subgraph contains all the nodes present in the original graph.
# The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
# It is also required that there is exactly one, exclusive path between any two nodes of the subgraph.
# One specific node  is fixed as the starting point of finding the subgraph using Prim's Algorithm.
# Find the total weight or the sum of all edges in the subgraph.

# Example



# image

# Starting from node , select the lower weight edge, i.e. , weight .

# Choose between the remaining edges, , weight , and , weight .

# The lower weight edge is  weight .

# All nodes are connected at a cost of . The edge  is not included in the subgraph.

# Function Description

# Complete the prims function in the editor below.

# prims has the following parameter(s):

# int n: the number of nodes in the graph
# int edges[m][3]: each element contains three integers, two nodes numbers that are connected and the weight of that edge
# int start: the number of the starting node
# Returns

# int: the minimum weight to connect all nodes in the graph
# Input Format

# The first line has two space-separated integers  and , the number of nodes and edges in the graph.

# Each of the next  lines contains three space-separated integers ,  and , the end nodes of , and the edge's weight.
# The last line has an integer , the starting node.

# Constraints





# There may be multiple edges between two nodes.

# Sample Input 0

# 5 6
# 1 2 3
# 1 3 4
# 4 2 6
# 5 2 2
# 2 3 5
# 3 5 7
# 1
# Sample Output 0

# 15
# Explanation 0

# The graph given in the test case is shown as :

# image

# The starting node is  (in the given test case)
# Applying the Prim's algorithm, edge choices available at first are :

#  (WT. 3) and  (WT. 4) , out of which  is chosen (smaller weight of edge).

# Now the available choices are :

#  (WT. 4) ,  (WT. 5) ,  (WT. 2) and  (WT. 6) , out of which  is chosen by the algorithm.

# Following the same method of the algorithm, the next chosen edges , sequentially are :

#  and .

# Hence the overall sequence of edges picked up by Prim's are:


# and the total weight of the MST (minimum spanning tree) is : 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    # Write your code here
    mst = {start}
    total = 0
    edges.sort(key=lambda x: x[2])

    # Prim: Add lowest weight edge that starts anywhere in the mst and ends on any of the remaining vertices (guarantees no cycles), until no vertices remain.
    while len(mst) < n:
        for u, v, w in edges:
            if (u in mst) ^ (v in mst):
                mst = mst.union({u, v})
                total += w
                break
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
