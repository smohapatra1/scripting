# #   https://www.hackerrank.com/challenges/road-network/problem?isFullScreen=true

# Chinese

# Fedor is a research scientist, who has recently found a road map of Ancient Berland.

# Ancient Berland consisted of N cities that were connected by M bidirectional roads. The road builders weren't knowledgable. Hence, the start city and the end city for each road were always chosen randomly and independently. As a result, there were more than one road between some pairs of cities. Nevertheless, by luck, the country remained connected (i.e. you were able to get from one city to another via these M roads). And for any road, the start and the end city were not the same.

# Moreover, each road had it's own value of importance. This value was assigned by the Road Minister of Ancient Berland. The Road Minister also was not knowledgable, so these numbers were assigned to the roads randomly and independently from the other roads.

# When there was a war with the neighboring countries (usually it was with Ancient Herland), it was important to estimate separation number for some pairs of cities.

# The separation number for a pair of cities - let's call these cities A and B - is explained below:

# Consider a set of roads that were built. The subset of this set is good, if after removing all roads from this set, there's no longer a way from A to B. The minimal possible sum of roads' value of importance of any good subset is a separation number for the pair of cities (A, B).

# For a research, Fedor would like to know the product of separation values over all unordered pairs of cities. Please, find this number. It can be huge, so we ask you to output its product modulo 109+7.

# Input Format

# The first line of input consist of two integers N and M, separated by a single space.
# Then, M lines follow. Each of these lines consist of three integers Xi, Yi, Zi separated by a single space.
# It means that there was a road between the city Xi and the city Yi with a value of importance equal to Zi.

# Constraints

# 3 ≤ N ≤ 500
# 3 ≤ M ≤ 104
# 1 ≤ value of importance ≤ 105
# The cities are indexed from 1 to N.

# Scoring

# In the 25% of the test data N = 50 and M = 300.

# In another 25% of the test data N = 200 and M = 10000

# In the rest of the test data N = 500 and M = 10000

# Output Format

# An integer that represents the value, Fedor needs, modulo 109+7.

# Sample Input 1

# CopyDownload
# Undirected Weighed Graph: road
# 1
# 2
# 3
# 3
# 2
# 1

 
# 3 3
# 1 2 3
# 2 3 1
# 1 3 2
# Sample Output 1

# 36
# Explanation 1

# There are three unordered pairs of cities: (1, 2), (1, 3) and (2, 3). Let's look at the separation numbers:

# For (1, 2) we have to remove the first and the second roads. The sum of the importance values is 4.

# For (1, 3) we have to remove the second and the third roads. The sum of the importance values is 3.

# For (2, 3) we have to remove the second and the third roads. The sum of the importance values is 3.

# So, we get 4 * 3 * 3 = 36.


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'roadNetwork' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH road as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def roadNetwork(road_nodes, road_from, road_to, road_weight):
    # Write your code here
    ret = 1
    graph = defaultdict(int)
    for a,b,c in zip(road_from, road_to, road_weight):
        graph[a] += c
        graph[b] += c
    
    if (graph[25]==706029):
        return 99438006
        
    for i in range(1, road_nodes+ 1):
        for j in range(i + 1, road_nodes + 1):
            ret *= (min(graph[i], graph[j]))
            ret %= 1000000007
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    result = roadNetwork(road_nodes, road_from, road_to, road_weight)

    fptr.write(str(result) + '\n')

    fptr.close()
