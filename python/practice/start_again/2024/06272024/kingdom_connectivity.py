# https://www.hackerrank.com/challenges/kingdom-connectivity/problem?isFullScreen=true

# It has been a prosperous year for King Charles and he is rapidly expanding his empire. In fact, he recently invaded his neighboring country and set up a new kingdom! This kingdom has many cities connected by one-way roads. To ensure higher connectivity, two cities are sometimes directly linked by more than one road.

# In the new kingdom, King Charles has made one of the cities his financial capital and another city his warfare capital. He wants a better connectivity between these two capitals. The connectivity of a pair of cities,  and , is defined as the number of different paths from city  to city . A path may use a road more than once if possible. Two paths are considered different if they do not use the same sequence of roads the same number of times.

# There are  cities numbered  to  in the new kingdom and  one-way roads. City  is the financial capital and city  is the warfare capital. Determine the number of different paths between cities  and . Since the number may be large, print the result modulo  or .

# Note: Two roads may connect the same cities, but they are still considered distinct for path connections.

# For example, there are  cities connected by  roads as shown in the following graph:

# image

# There are two direct paths and one cyclic path. Direct paths are  and  and . The cycle  can be repeated any number of times, so there are infinite paths. If the connection  did not exist, there would be only the two direct paths.

# Function Description

# Complete the countPaths function in the editor below. It should print your result, modulo  if there are limited paths or INFINITE PATHS if they are unlimited. There is no expected return value.

# countPaths has the following parameters:
# - n: the integer number of cities
# - edges: a 2D integer array where  is the source city and  is the destination city for the directed road 

# Input Format

# The first line contains two integers  and .
# Each of the following  lines contains two space-separated integers that represent source and destination cities for a directed connection.

# Constraints

# Output Format

# Print the number of different paths from city  to city  modulo . If there are infinitely many different paths, print INFINITE PATHS.

# Sample Input

# Sample Input 0

# 5 5  
# 1 2  
# 2 4  
# 2 3  
# 3 4  
# 4 5
# Sample Output 0

# 2
# Explanation 0

# image

# There are two possible paths from city  to city :


# Sample Input 1

# 5 5  
# 1 2  
# 4 2  
# 2 3  
# 3 4  
# 4 5
# Sample Output 1

# INFINITE PATHS 
# Explanation 1

# image

# The cycle in the graph can be traversed an infinite number of times on the way to city .

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'countPaths' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def triTopo(n,graph,onThePath):
    numero = []
    color = [0 for _ in range(n)]
    for sommet in range(n):
        if sommet in onThePath and color[sommet] == 0:
            if triTopoRec(graph,numero,color,sommet):
                return ([],True)
    return (numero,False)

def triTopoRec(graph,numero,color,sommet):
    color[sommet] = 1
    for voisin in graph[sommet]:
        if color[voisin] == 0:
            if triTopoRec(graph,numero,color,voisin):
                return True
        elif color[voisin] == 1:
            return True
    color[sommet] = 2
    numero.append(sommet)
    return False

def takeSecond(elem):
    return elem[1]

def countPaths(n, edges):
    # Write your code here
    graph = [set() for _ in range(n)]
    graphRevert = [set() for _ in range(n)]
    weight = defaultdict(int)
    for edge in edges:
        i,j = edge
        graph[i].add(j)
        graphRevert[j].add(i)
        weight[(i,j)] += 1

    accessibleFromStart = bfs(graph,0)
    accessibleFromEnd = bfs(graphRevert,n-1)
    onThePath = accessibleFromStart.intersection(accessibleFromEnd)
    
    if not onThePath:
        #No path between start and end
        print(0)
    else:
        newGraph = [set() for _ in range(n)]
        newGraphRevert = [set() for _ in range(n)]
        for edge in edges:
            i,j = edge
            if i in onThePath and j in onThePath:
                newGraph[i].add(j)
                newGraphRevert[j].add(i)
        
        ordre,infinite = triTopo(n,newGraph,onThePath)
        if infinite:
            print("INFINITE PATHS")
        else:
            ordre.reverse()
            nbChemins = [0 for _ in range(n)]
            nbChemins[0] = 1
            for sommet in ordre[1:]:
                for predec in newGraphRevert[sommet]:
                    nbChemins[sommet] += nbChemins[predec] * weight[(predec,sommet)]
            #The end:
            print(nbChemins[n-1]%(10**9))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    nodes = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(lambda x : int(x)-1, input().rstrip().split())))

    countPaths(nodes, edges)