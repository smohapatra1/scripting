# #   https://www.hackerrank.com/challenges/repair-roads/problem?isFullScreen=true

# The country of Byteland contains  cities and  bidirectional roads. There is a path between any two cities. The roads in Byteland were built long ago, and now they are in need of repair. You have been hired to fix all the roads. You intend to do this by dispatching robots on some of the roads. Each robot will repair the road he is currently on and then moves to one of the adjacent unrepaired roads. After repairing that, it will move to another adjacent unrepaired road, repair that and so on.

# Two roads are adjacent if they have the same city at one of their endpoints. For the process to be efficient, no two robots will ever repair the same road, and no road can be visited twice. What is the minimum number of robots needed to accomplish the task?

# Input Format

# The first line contains the number of test cases .  test cases follow. The first line of each test case contains , the number of cities in Byteland. The cities are numbered . The following  lines contain the description of the roads. The  line contains two integers  and , meaning that there is a road connecting cities with numbers  and .

# Constraints

# Output Format

# Print  lines, one corresponding to each test case containing the required answer for that test case.

# Sample Input

# 3  
# 4  
# 0 1  
# 0 2  
# 0 3  
# 6  
# 0 1  
# 1 2  
# 2 3  
# 2 4  
# 4 5  
# 7  
# 0 1  
# 1 2  
# 2 3  
# 2 4  
# 4 5  
# 3 6
# Sample Output

# 1  
# 1  
# 2
# Explanation

# For the first case, one robot is enough to repair all roads: 
# For the second case, one robot is again enough: 
# The the third case, there is no way to repair all the roads with one robot and at least two are needed.



#!/bin/python3

import math
import os
import random
import re
import sys
import collections
import queue

#
# Complete the 'repairRoads' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def solve():
    n = int(input().strip())

    # read graph
    graph = dict((i, []) for i in range(0, n))

    for j in range(n - 1):
        x, y = [int(p) for p in input().strip().split()]
        graph[x].append(y)
        graph[y].append(x)

    # transform graph into tree
    level = 1

    root = 0
    q = queue.Queue()
    q.put((root, level, None))
    seen = set([])

    levels = collections.defaultdict(set)
    tree = {}

    while not q.empty():
        item, level, parent = q.get()
        levels[level].add(item)
        seen.add(item)

        tree[item] = dict(id=item, parent=parent, level=level, children=set([]),
                          leaf=None)

        for child in graph[item]:
            if child not in seen:
                q.put((child, level + 1, item))
                seen.add(child)
                tree[item]['children'].add(child)

    # print('Levels: %s' % levels)
    # print('Tree: %s' % tree)

    # count clusters
    clusters = 1
    has_items_in_cluster = False

    for level in sorted(levels.keys(), reverse=True):
        for item in levels[level]:
            tree_item = tree[item]
            if not tree_item['children']:  # leaf
                tree_item['leaf'] = True
            else:
                has_items_in_cluster = True

                branches = 0
                for child in tree_item['children']:
                    if not tree[child]['leaf']:
                        branches += 1

                # branches == 0 -> visit point and go up
                # branches == 1 -> visit downstream, point and go up
                # branches % 2 == 0 -> have (branches // 2) clusters
                # branches % 2 == 1 -> have  (branches // 2) clusters and go up
                if branches >= 2:
                    new_clusters = branches // 2

                    clusters += new_clusters
                    # print('New clusters: %d' % new_clusters)

                    if branches % 2 == 0:
                        has_items_in_cluster = False
                        # cluster will also include road up
                        parent = tree_item['parent']
                        if parent is not None:
                            # print('Cut %s and %s' % (item, parent))
                            tree[parent]['children'].remove(item)

            # print(tree[item])

    # print('Tree: %s' % tree)

    if not has_items_in_cluster:
        clusters -= 1  # last cluster was created but has no items

    print(clusters)


t = int(input().strip())

for tt in range(t):
    solve()
    
    
    
# def repairRoads(n, roads):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         roads = []

#         for _ in range(n - 1):
#             roads.append(list(map(int, input().rstrip().split())))

#         result = repairRoads(n, roads)

#         fptr.write(str(result) + '\n')

#     fptr.close()
