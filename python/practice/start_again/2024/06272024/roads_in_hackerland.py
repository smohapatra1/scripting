# #   https://www.hackerrank.com/challenges/johnland/problem?isFullScreen=true

# John lives in HackerLand, a country with  cities and  bidirectional roads. Each of the roads has a distinct length, and each length is a power of two (i.e.,  raised to some exponent). It's possible for John to reach any city from any other city.

# Given a map of HackerLand, can you help John determine the sum of the minimum distances between each pair of cities? Print your answer in binary representation.

# Input Format

# The first line contains two space-seperated integers denoting  (the number of cities) and  (the number of roads), respectively.
# Each line  of the  subsequent lines contains the respective values of , , and  as three space-separated integers. These values define a bidirectional road between cities  and  having length .

# Constraints

# , 
# If , then .
# Output Format

# Find the sum of minimum distances of each pair of cities and print the answer in binary representation.

# Sample Input

# 5 6
# 1 3 5
# 4 5 0
# 2 1 3
# 3 2 1
# 4 3 4
# 4 2 2
# Sample Output

# 1000100
# Explanation

# In the sample, the country looks like this:

# image

# Let  be the minimum distance between city  and city .


#!/bin/python3

import math
import os
import random
import re
import sys
import heapq as hq

#
# Complete the 'roadsInHackerland' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def find_other(t, i):
    """
        given a tuple (a,b) and 'i' equal to one of them, it returns
        the other value. i.e. if i==a, return 'b' and vice-versa
    """
    if i == t[0]:
        return t[1]
    elif i == t[1]:
        return t[0]
    else:
        return None


#
# Complete the roadsInHackerland function below.
#
def roadsInHackerland(n, roads):
    #
    # Write your code here.
    #
    #base_time = time.time()
    ### largest cost in the resulting MST. used to size the list
    max_cost = 0
    
    ### MST edges. key is tuple (i,j); i<j.  value is the edge'cost',
    edges_cost = dict()
    
    ### list of edges in which the node is part has in the resulting MST
    ### first entry is the number of 'unsolved' edges for the node
    MST_neigh = [[0, []] for _ in range(n)]
    
    ### nodes already added to graph
    added = set([0]);
    
    ### working heap list of tuples (distance, i, j)
    ws = []
    for j,dist in roads[0].items():
        ws.append((dist, 0, j))
    hq.heapify(ws)
    #ws.sort(reverse=True)

    while len(added) < n:
        ### retrive the smallest egde
        #dist,a,b = hq.heappop(ws)
        dist,a,b = hq.heappop(ws)
        
        if a > b:
            a,b = b,a
        if not a in added:
            i = a
        elif not b in added:
            i = b
        else:
            continue

        ### 'na' and 'nb' are calculated later
        edges_cost[(a,b)] = dist
        if dist > max_cost:
            max_cost = dist
        added.add(i)
        MST_neigh[a][0] += 1
        MST_neigh[b][0] += 1
        MST_neigh[a][1].append((a,b))
        MST_neigh[b][1].append((a,b))
        
        for j,dist in roads[i].items():
            if not j in added:
                #ws.append((dist, i, j))
                hq.heappush(ws, (dist, i, j))
        #hq.heapify(ws)
        

    #print("done w/ MST:   ", time.time()-base_time)
    #base_time = time.time()    
    ### find the number of nodes in subtrees on both sides of each edge 
    ### start with nodes having 1 unsolved edge
    
    ### number of nodes in each subtree on both side of an egde
    ### key: (i,j);  value dictionary of {i:nodes, j:nodes}
    edges_nodes = dict()
    
    ### list of nodes to process -add all nodes with 1 unsolved edge
    ws = []
    for node, item in enumerate(MST_neigh):
        if item[0] == 1:
            ws.append((node,item))
    
    while len(ws) > 0:
        me, item = ws.pop(0)
        tmp = 1                 # keeps track of number of nodes
        unsolved = None         # store the 1 unsolved edge
        
        ### avoid processing the very last edge twice
        if item[0] < 1:
            continue
        
        for edge in item[1]:    # walk the edge list
            if edge in edges_nodes:     # already solved
                tmp += edges_nodes[edge][find_other(edge, me)]
            else:
                unsolved = edge

        peer_node = find_other(unsolved, me)    # the other end of unsolved edge
        ### add to number of nodes per edge dict.
        edges_nodes[unsolved] = {me:tmp, peer_node:(n-tmp)}

        ### decrement the number of unsolved nodes
        item[0] -= 1        # this should end up 0
        MST_neigh[peer_node][0] -= 1
        
        ### if the other node only has one unsolved edge, add it to list
        if MST_neigh[peer_node][0] == 1:
            ws.append((peer_node, MST_neigh[peer_node]))

#    for item in enumerate(MST_neigh):
#        print(item)
#    for item in edges_cost.items():
#        print(item)
#    for item in edges_nodes.items():
#        print(item)
    #print("done w/ tree:  ", time.time()-base_time)
    #base_time = time.time()
        
    ### create a list holding the bit for each position
    ### largest number of times using an edge is (n/2)^2.
    ### that is 25Mil, which fits in 25 bits (24.575)
    res = [0] * (max_cost+25)
    
    for edge,i in edges_cost.items():
        ### number a times an edge is traveresed
        count = 1
        for num in edges_nodes[edge].values():
            count *= num
        while count > 0:
            if count & 1:
                res[i] += 1
            count >>= 1
            i += 1
#    print(res)
    ### reduce result's list elements to binary
    max_bit_set = 0
    for i in range(len(res)):
        if res[i] > 1:
            res[i+1] += (res[i]>>1)
            res[i] &= 1
        if (res[i] == 1):
            max_bit_set = i
    
    res = res[:max_bit_set+1]
    res.reverse()
    
    #print("done w/ binary:", time.time()-base_time)
    
    return "".join([str(i) for i in res])

if __name__ == '__main__':
    n, m = [int(i) for i in input().strip().split()]

    #base_time = time.time()
    roads = [dict() for _ in range(n)]

    for _ in range(m):
        i, j, dist = list(map(int, input().rstrip().split()))
        i,j = i-1, j-1
        if (not j in roads[i]) or (roads[i][j] > dist):
            roads[i][j] = dist
            roads[j][i] = dist

    #print("done reading:  ", time.time()-base_time)
    print(roadsInHackerland(n, roads))
    
    

# def roadsInHackerland(n, roads):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     roads = []

#     for _ in range(m):
#         roads.append(list(map(int, input().rstrip().split())))

#     result = roadsInHackerland(n, roads)

#     fptr.write(result + '\n')

#     fptr.close()
