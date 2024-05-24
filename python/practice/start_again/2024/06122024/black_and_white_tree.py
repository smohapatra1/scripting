# #   https://www.hackerrank.com/challenges/black-n-white-tree-1/problem?isFullScreen=true

# Nikita is making a graph as a birthday gift for her boyfriend, a fellow programmer! She drew an undirected connected graph with  nodes numbered from  to  in her notebook.

# Each node is shaded in either white or black. We define  to be the number of white nodes, and  to be the number of black nodes. The graph is drawn in such a way that:

# No  adjacent nodes have same coloring.
# The value of , which we'll call , is minimal.
# Nikita's mischievous little brother erased some of the edges and all of the coloring from her graph! As a result, the graph is now decomposed into one or more components. Because you're her best friend, you've decided to help her reconstruct the graph by adding  edges such that the aforementioned graph properties hold true.

# Given the decomposed graph, construct and shade a valid connected graph such that the difference  between its shaded nodes is minimal.

# Input Format

# The first line contains  space-separated integers,  (the number of nodes in the original graph) and  (the number of edges in the decomposed graph), respectively.
# The  subsequent lines each contain  space-separated integers,  and , describing a bidirectional edge between nodes  and  in the decomposed graph.

# Constraints

# It is guaranteed that every edge will be between  distinct nodes, and there will never be more than  edge between any  nodes.
# Your answer must meet the following criteria:
# The graph is connected and no  adjacent nodes have the same coloring.
# The value of  is minimal.
# Output Format

# You must have  lines of output. The first line contains  space-separated integers:  (the minimum possible value of ) and  (the number of edges you've added to the graph), respectively.
# Each of the  subsequent lines contains  space-separated integers,  and , describing a newly-added bidirectional edge in your final graph (i.e.: new edge ).

# You may print any  of the possible reconstructions of Nikita's graph such that the value of  in the reconstructed shaded graph is minimal.

# Sample Input 0

#  8 8
#  1 2
#  2 3
#  3 4
#  4 1
#  1 5
#  2 6
#  3 7
#  4 8
# Sample output 0

# 0 0
# Sample Input 1

#  8 6
#  1 2
#  3 4
#  3 5
#  3 6
#  3 7
#  3 8
# Sample Output 1

# 4 1
# 1 5
# Sample Input 2

#  5 4
#  1 2
#  2 3
#  3 4
#  4 1
# Sample Output 2

#   1 2
#   2 5
#   4 5
# Explanation

# In the figure below, the solid lines show the decomposed graph after Nikita's brother erased the edges, and the dotted lines show one possible correct answer:

# bw.jpg

# In Sample , no additional edges are added and . Because  and , we get . Thus, we print  on a new line (there is only  line of output, as ).

# In Sample , the only edge added is , so . Here,  and , so . Thus, we print  on the first line. Next, we must print  lines describing each edge added; because , we print a single line describing the  space-separated nodes connected by our new edge: .

# In Sample , we can either add  edge  or , or both of them. In both cases we get  and , so . Thus  and  or  both are correct.


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

#
# Complete the 'blackWhiteTree' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts UNWEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

sys.setrecursionlimit(10**6)
def blackWhiteTree(g_nodes, g_from, g_to):
    # Write your code here
    d = defaultdict(list)
    visited = [False] * (1 + g_nodes)
    root = [None] * (1 + g_nodes)
    tree_diff = defaultdict(list)  
    valid_roots = []
    res = []    
    
    for i, j in zip(g_from, g_to):
        d[i].append(j)
        d[j].append(i)
  
    def bfs(i, color):
        if not visited[i]:
            q = deque()
            q.append((i, color))   
            root[i] = [0, 0, 0, 0, False, False, False]
            while q:
                l = len(q)
                for j in range(l):
                    u, f = q.popleft()
                    if not visited[u]: # to handle cycle
                        visited[u] = True
                        root[i][f] += 1
                        root[i][2 + f] = u                        
                        for v in d[u]:
                            if not visited[v]:
                                q.append((v, not f))
    
    max_diff = 0
    all_diff = [0] * (g_nodes + 1)
    no_of_trees = 0
    for i in range(1, g_nodes + 1):
        #dfs(i, visited.get(i, True), i)
        bfs(i, True)
        if root[i]:
            valid_roots.append(i)
            no_of_trees += 1
            diff = root[i][1] - root[i][0] #c(i, True) - c(i, False)
            if diff > 0:
                root[i][5] = True
            elif diff < 0:
                root[i][4] = True
                
            diff = abs(diff)
            tree_diff[diff].append(i)
            all_diff[diff] += 1
            max_diff += diff
    
    N = 1 + max_diff
    possible_diff = [N] * (1 + max_diff)
    possible_diff[0] = 0
    parent_diff = [0] * (1 + max_diff)
    parent_diff[0] = 0
    for i, flg in enumerate(all_diff):
        if i and flg:
            for j in range(1 + max_diff - i):
                if possible_diff[i + j] == N and possible_diff[j] != N:
                    possible_diff[i + j] = 1 + possible_diff[j]
                    parent_diff[i + j] = j
            
            for j in range(1, 1 + max_diff):
                if flg < possible_diff[j]:
                    possible_diff[j] = N
                    parent_diff[j] = 0
                else:
                    possible_diff[j] = 0
                    
    
    min_diff = max_diff
    diff = 0
    for i, d in enumerate(possible_diff):
        if d < N:
            t = abs(max_diff - 2 * i)
            if min_diff >= t:
                min_diff = t
                diff = i
    
    #true_major, false_major = set(), set()
    while diff > 0:
        i = tree_diff[diff - parent_diff[diff]].pop()
        root[i][6] = True
        if root[i][4]: # c(i, True) < c(i, False):
            root[i][0], root[i][1], root[i][2], root[i][3], root[i][4], root[i][5] = \
                root[i][1], root[i][0], root[i][3], root[i][2], root[i][5], root[i][4] 
        diff = parent_diff[diff]
    
    for i in valid_roots:
        #false_major.add(i)
        if not root[i][6] and root[i][5]: #c(i, False) < c(i, True):
            root[i][0], root[i][1], root[i][2], root[i][3], root[i][4], root[i][5] = \
                root[i][1], root[i][0], root[i][3], root[i][2], root[i][5], root[i][4]          
    
    res.append("{} {}".format(min_diff, no_of_trees - 1))
    true_node, false_node, root_true_node, root_false_node = -1, -1, -1, -1
    for i in valid_roots:
        if root[i][3]:
            true_node = root[i][3]
            root_true_node = i
        
        if root[i][2]:
            false_node = root[i][2]
            root_false_node = i
            
        if true_node != -1 and false_node != -1:
            break
    
    if root_true_node != root_false_node:
        res.append("{} {}".format(true_node, false_node))
        
    for i in valid_roots:
        if i ^ root_true_node and i ^ root_false_node:
            if root[i][3]:
                res.append("{} {}".format(false_node, root[i][3]))
            elif root[i][2]:
                res.append("{} {}".format(true_node, root[i][2]))
    #res = map(lambda x : " ".join(map(str, x)), res)
    return res


# def blackWhiteTree(g_nodes, g_from, g_to):
#     # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i] = map(int, input().rstrip().split())

    result = blackWhiteTree(g_nodes, g_from, g_to)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
