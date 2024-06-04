# https://www.hackerrank.com/challenges/jeanies-route/problem?isFullScreen=true

# Byteland has  cities (numbered from  to ) and  bidirectional roads. It is guaranteed that there is a route from any city to any other city.

# Jeanie is a postal worker who must deliver  letters to various cities in Byteland. She can start and end her delivery route in any city. Given the destination cities for  letters and the definition of each road in Byteland, find and print the minimum distance Jeanie must travel to deliver all  letters.

# Note: The letters can be delivered in any order.

# Input Format

# The first line contains two space-separated integers,  (the number of cities) and  (the number of letters), respectively.
# The second line contains  space-separated integers describing the delivery city for each letter.
# Each line  of the  subsequent lines contains  space-separated integers describing a road as , where  is the distance (length) of the bidirectional road between cities  and .

# Constraints

# Output Format

# Print the minimum distance Jeanie must travel to deliver all  letters.

# Sample Input 0

# 5 3
# 1 3 4
# 1 2 1
# 2 3 2
# 2 4 2
# 3 5 3
# Sample Output 0

# 6
# Explanation 0

# Jeanie has  letters she must deliver to cities , , and  in the following map of Byteland: jub1.png

# One of Jeanie's optimal routes is , for a total distanced traveled of . Thus, we print  on a new line.

#!/bin/python3

import os
import sys

#
# Complete the jeanisRoute function below.
#

def dfs(root, adj, nodes):
    parent = {root: None}
    depth = {root: 0}
    dist = {root: 0}
    
    stack = [root]
    while len(stack):
        curr = stack.pop()
        curr_depth = depth[curr]
        curr_dist = dist[curr]
        
        for nei in adj[curr]:
            if nei != parent[curr] and nei in nodes:
                parent[nei] = curr
                depth[nei] = curr_depth + 1
                dist[nei] = curr_dist + adj[curr][nei]
                stack.append(nei)
        
    return parent, depth, dist

n, k = map(int, input().split())
targets = set(map(int, input().split()))

nodes = set(range(1, n + 1))
adj = {x: dict() for x in nodes}
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    adj[a][b] = c
    adj[b][a] = c
    
parent, depth, dist = dfs(list(targets)[0], adj, nodes)

nodes_sorted = sorted(nodes, key=lambda x: depth[x], reverse=True)
for node in nodes_sorted:
    num_connected = len([x for x in adj[node] if x in nodes])
    if node not in targets and num_connected == 1:
        nodes.remove(node)
        del adj[node]

furthest_node = max(nodes, key=lambda x: dist[x])

# Re-root the tree at the last node
parent, depth, dist = dfs(furthest_node, adj, nodes)

# Get the new furthest
furthest_node = max(nodes, key=lambda x: dist[x])
largest_distance = dist[furthest_node]

tot_sum = 0
for node in nodes:
    for nei in adj[node]:
        if nei in nodes:
            tot_sum += adj[node][nei]

print(tot_sum - largest_distance)


# def jeanisRoute(k, roads):
#     #
#     # Write your code here.
#     #

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nk = input().split()

#     n = int(nk[0])

#     k = int(nk[1])

#     city = list(map(int, input().rstrip().split()))

#     roads = []

#     for _ in range(n-1):
#         roads.append(list(map(int, input().rstrip().split())))

#     result = jeanisRoute(k, roads)

#     fptr.write(str(result) + '\n')

#     fptr.close()

