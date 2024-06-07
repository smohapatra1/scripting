# #   https://www.hackerrank.com/challenges/savita-and-friends/problem?isFullScreen=true

# After completing her final semester, Savita is back home. She is excited to meet all her friends. Her  friends live in different houses spread across the city.

# There are  roads connecting the houses. The road network formed is connected and does not contain self loops and multiple roads between same pair of houses. Savita and Friends decide to meet.

# Savita wants to choose a point(not necessarily an integer)  on the road numbered , such that, the maximum of  for all  is minimised,
# where  is the shortest distance between the 'th friend and .

# If 'th road connects friend  and friend  you should print distance of chosen point from . Also, print the  for all . If there is more than one solution, print the one in which the point  is closest to .

# Note:

# Use scanf/printf instead of cin/cout. Large input files.
# Order of  and  as given in the input must be maintained. If P is at a distance of 8 from  and 2 from , you should print 8 and not 2.
# Input Format

# First line contain , the number of testcases.
# T testcases follow.
# First Line of each testcase contains 3 space separated integers  .
# Next  lines contain description of the th road : three space separated integers , where  is the length of road connecting  and .

# Constraints







# Output Format

# For each testcase, print two space separated values in one line. The first value is the distance of  from the point  and the second value is the maximum of all the possible shortest paths between  and all of Savita's and her friends' houses. Round both answers to  decimal digits and print exactly  digits after the decimal point.

# Sample Input

# 2
# 2 1 1
# 1 2 10
# 4 4 1
# 1 2 10
# 2 3 10
# 3 4 1
# 4 1 5
# Sample Output

# 5.00000 5.00000
# 2.00000 8.00000
# Explanation

# First testcase:
# As  = 1, they will meet at the point  on the road that connects friend  with friend . If we choose mid point then distance for both of them will be . In any other position the maximum of distance will be more than .

# Second testcase:
# As  = 1, they will meet at a point  on the road connecting friend  and friend . If we choose point at a distance of  from friend : Friend  will have to travel distance .
# Friend  will have to travel distance .
# Friend  will have to travel distance .
# Friend  will have to travel distance .
# So, the maximum will be .
# In any other position of point choosen, the maximum distance will be more than .

# Timelimits

# Timelimits for this problem is 2 times the environment limit.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY roads
#
from collections import defaultdict

def dijkstra(neighbors, start):
    import heapq

    seen = set()
    dist = {start: 0}
    suivants = [(0, start)] # tas de couples (d[x],x)

    while suivants != []:

        dx, x = heapq.heappop(suivants)
        if x in seen:
            continue

        seen.add(x)

        for y, d in neighbors[x]:
            if y in seen:
                continue
            dy = dx + d
            if y not in dist or dist[y] > dy:
                dist[y] = dy
                heapq.heappush(suivants, (dy, y))
    return dist


def get_objective_function(dist_a, dist_b, dist_ab):

    def prune(cusps):
        cusps = sorted(cusps, key=lambda x: x[1], reverse=True)
        out = [cusps[0]]
        for x, y in cusps[1:]:
            if any(y0 - y >= abs(x0 - x) for x0, y0 in out):
                continue
            out.append((x, y))
        return out

    def remove_useless_outliers(cusps):
        # keep cusps that bracket the interval [0, dist_ab], do not remove
        # those further away
        cusps = sorted(cusps, key=lambda x: x[0])
        n1 = 0
        n2 = 0
        for x, y in cusps:
            if x <= 0:
                n1 += 1
            elif x >= dist_ab:
                n2 += 1
        return cusps[max(n1-1, 0):-(n2 - 1) if n2 > 1 else len(cusps)]

    def objective_function(x):
        return max(min(da + x, db + dist_ab - x)
                   for da, db in zip(dist_a, dist_b))


    cusps = []
    for da, db in zip(dist_a, dist_b):
        if da < math.inf and db < math.inf:
            cusp = (db - da + dist_ab) / 2, (da + db + dist_ab) / 2
            if cusp[0] < 0:
                cusp = 0, db + dist_ab
            elif cusp[0] > dist_ab:
                cusp = dist_ab, da + dist_ab
        elif da < math.inf:
            cusp = dist_ab, da + dist_ab
        elif db < math.inf:
            cusp = 0, db + dist_ab
        else:
            raise ValueError('A node is not connected to the targets.')
        cusps.append(cusp)

    cusps = prune(cusps)
    cusps = remove_useless_outliers(cusps)
    return objective_function, cusps


def get_local_minima(cusps, dist_ab):
    mins = []
    x1, y1 = cusps[0]

    if x1 > 0:
        mins.append((0, y1 - x1))

    for i, (x2, y2) in enumerate(cusps[1:]):
        x0 = (x1 + x2 + y1 - y2) / 2
        y0 = (x1 - x2 + y1 + y2) / 2
        mins.append((x0, y0))
        x1, y1 = x2, y2

    x2, y2 = cusps[-1]
    if x2 < dist_ab:
        mins.append((dist_ab, x2 + y2 - dist_ab))

    return mins

def solve(n, k, roads,debug=False):
    # Write your code here
    edges = roads.copy()
    target_a, target_b, dist_ab = edges[k-1]
    edges.pop(k-1)
    edges.extend([(r, l, c) for l, r, c in edges])
    neighbors = defaultdict(list)
    for l, r, c in edges:
        neighbors[l].append((r, c))

    dist_a = n * [math.inf]
    for node, dist in dijkstra(neighbors, target_a).items():
        dist_a[node-1] = dist
    dist_b = n * [math.inf]
    for node, dist in dijkstra(neighbors, target_b).items():
        dist_b[node-1] = dist
    func, cusps = get_objective_function(dist_a, dist_b, dist_ab)
    minima = get_local_minima(cusps, dist_ab)

    x = sorted(minima, key=lambda x: math.floor(x[1]*1e7))[0]
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        k = int(first_multiple_input[2])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        result = solve(n, k, roads)

        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')
        fptr.write('{0[0]:.5f} {0[1]:.5f}\n'.format(result))

    fptr.close()
