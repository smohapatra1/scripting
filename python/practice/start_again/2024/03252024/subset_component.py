# #   https://www.hackerrank.com/challenges/subset-component/problem?isFullScreen=true

# You are given an array with  -bit integers: .

# BIT(x, i) = (x >> i) & 1, where  is the  lower bit of  in binary form. If we regard every bit as a vertex of a graph G, there is an undirected edge between vertices  and  if there is a value  such that BIT(d[k], i) == 1 && BIT(d[k], j) == 1.

# For every subset of the input array, how many connected-components are there in that graph?

# A connected component in a graph is a set of nodes which are accessible to each other via a path of edges. There may be multiple connected components in a graph.

# Example

# In the real challenge, there will be  nodes associated with each integer in  represented as a  bit binary value. For clarity, only  bits will be shown in the example but all  will be considered in the calculations.

#     Decimal  Binary Edges   Node ends
#     d[0] = 1   0001   0
#     d[1] = 2   0010   0
#     d[2] = 3   0011   1       0 and 1
#     d[3] = 5   0101   1       0 and 2
# Consider all subsets:

#                  Edges
#     Subset   Count  Nodes  Connected components
#     {1}         0           64
#     {2}         0           64
#     {3}         1   0-1     63
#     {5}         1   0-2     63
#     {1,2}       0           64
#     {1,3}       1   0-1     63
#     {1,5}       1   0-2     63
#     {2,3}       1   0-1     63
#     {2,5}       1   0-2     63
#     {3,5}       2   0-1-2   62
#     {1,2,3}     1   0-1     63
#     {1,2,5}     1   0-2     63
#     {1,3,5}     2   0-1-2   62
#     {2,3,5}     2   0-1-2   62
#     {1,2,3,5}   2   0-1-2   62
#     Sum                    944
# The values  and  have  bits set, so they have  edge each. If a subset contains only a  or , there will be one connected component with  nodes, and  components with  node for a total of .

# If both  and  are in a subset,  component with nodes  and  is formed since node  is one end of each edge described. The other  nodes are solitary, so there are  connected components total.

# All other values have only  bit set, so they have no edges. They have  components with  node each.

# Function Description

# Complete the findConnectedComponents function in the editor below.

# findConnectedComponents has the following parameters:

# int d[n]: an array of integers
# Returns

# int: the sum of the number of connected components for all subsets of 
# Input Format

# The first row contains the integer , the size of .
# The next row has  space-separated integers, .

# Constraints



# Sample Input 1

# CopyDownload
# Array: d
# 2
# 5
# 9

 
# 3
# 2 5 9
# Sample Output 1

# 504

# Explanation 1

# There are  subset of .

# {}
# => We don't have any number in this subset => no edge in the graph => Every node is a component by itself => Number of connected-components = 64.

# {2}
# => The Binary Representation of 2 is . There is a bit at only one position. => So there is no edge in the graph, every node is a connected-component by itself => Number of connected-components = 64.

# {5}
# => The Binary Representation of 5 is . There is a bit at the 0th and 2nd position. => So there is an edge: (0, 2) in the graph => There is one component with a pair of nodes (0,2) in the graph. Apart from that, all remaining 62 vertices are indepenent components of one node each (1,3,4,5,6...63) => Number of connected-components = 63.

# {9}
# => The Binary Representation of 9 is . => There is a 1-bit at the 0th and 3rd position in this binary representation. => edge: (0, 3) in the graph => Number of components = 63

# {2, 5}
# => This will contain the edge (0, 2) in the graph which will form one component
# => Other nodes are all independent components
# => Number of connected-component = 63

# {2, 9}
# => This has edge (0,3) in the graph
# => Similar to examples above, this has 63 connected components

# {5, 9}
# => This has edges (0, 2) and (0, 3) in the graph
# => Similar to examples above, this has 62 connected components

# {2, 5, 9}
# => This has edges(0, 2) (0, 3) in the graph. All three vertices (0,2,3) make one component => Other 61 vertices are all independent components
# => Number of connected-components = 62



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findConnectedComponents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY d as parameter.
#

def findConnectedComponents(d):
    # Write your code here
    sols=0
    for bit in range(64):
        n_unset = sum(i & (1 << bit ) <= 0 for i in d )
        sols += 2 ** n_unset
    return sols + 2 ** len(d) -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input().strip())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()


