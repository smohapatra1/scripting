#   https://www.hackerrank.com/test/3g7sntr46mr/questions/4rcfp2hh0ge

#!/bin/python3

import math
import os
import random
import re
import sys
import queue
from collections import deque



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    # Map the nodes to be 0-indexed
    s -= 1
    edges = [(e[0]-1, e[1]-1) for e in edges]
    
    # Set initial distances.
    distances = [-1 for i in range(n)]
    distances[s] = 0
    
    # Create adjacency matrix.
    adj = {i : set() for i in range(n)}
    for i,j in edges:
        adj[i].add(j)
        adj[j].add(i)
    
    # Use a deque datastructure, as it is more efficient
    # for representing a queue in Python. Push at the 
    # right side and pop from the left side.
    queue = deque()
    queue.append(s)
    
    while(queue):
        node = queue[0]
        
        # Get the neighboring nodes, then filter to unvisited nodes.
        n_nodes   = adj[node]
        u_n_nodes = [n for n in n_nodes if distances[n] < 0]
        
        for n in u_n_nodes:
            distances[n] = distances[node] + 6
            queue.append(n)

        queue.popleft()

    # Do not include the start node 
    distances.pop(s)
    return distances
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
        #print (result)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
