# #   https://www.hackerrank.com/challenges/bytelandian-tours/problem?isFullScreen=true



# The country of Byteland contains N cities and N - 1 bidirectional roads between them such that there is a path between any two cities. The cities are numbered (0,...,N - 1). The people were very unhappy about the time it took to commute, especially salesmen who had to go about every city selling goods. So it was decided that new roads would be built between any two "somewhat near" cities. Any two cities in Bytleland that can be reached by traveling on exactly two old roads are known as "somewhat near" each other.

# Now a salesman situated in city 0, just like any other typical salesman, has to visit all cities exactly once and return back to city 0 in the end. In how many ways can he do this?

# Input Format

# The first line contains the number of test cases T. T test cases follow. The first line contains N, the number of cities in Byteland. The following N - 1 lines contain the description of the roads. The ith line contains two integers ai and bi, meaning that there was originally a road connecting cities with numbers ai and bi.

# Constraints

# 1 <= T <= 20
# 1 <= N <= 10000
# 0 <= ai,bi < N  

# Output Format

# Output T lines, one corresponding to each test case containing the required answer for that test case. Since the answers can be huge, output them modulo 1000000007.

# Sample Input

# 2
# 3
# 0 1
# 1 2
# 5
# 0 1
# 1 2
# 2 3
# 2 4

# Sample Output

# 2
# 4

# Explanation

# For the first case, a new road was build between cities 0 and 2. Now, the salesman has two tour possibilities: 0-1-2-0 or 0-2-1-0.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bytelandianTours' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def bytelandianTours(n, roads):
    # Write your code here
    if n <= 2:
        return 1
    m = 1000000007
    nbr = list()
    for i in range(n):
        nbr.append(list())
    for a,b in roads:
        nbr[a].append(b)
        nbr[b].append(a)
    
    city = 0
    if len(nbr[0]) == 1:
        city = nbr[0][0]
    nbr[city].sort(key=lambda x: len(nbr[x]), reverse = True)
    if len(nbr[nbr[city][0]]) == 1:
        return math.factorial(len(nbr[city])) % m
    if len(nbr[city]) > 2 and len(nbr[nbr[city][2]]) > 1:
        return 0
    if len(nbr[nbr[city][1]]) > 1:
        next_route = nbr[city][1]
        nbr[next_route].remove(city)
        rslt = (2 * math.factorial(len(nbr[city]) - 2)) % m
    else:
        next_route = -1
        rslt = (2 * math.factorial(len(nbr[city]) - 1)) % m
    #print(city, nbr)
    parent = city
    city = nbr[city][0]
    nbr[city].remove(parent)
    while True:
        nbr[city].sort(key=lambda x: len(nbr[x]), reverse = True)
        #print(city, nbr)
        if len(nbr[nbr[city][0]]) == 1:
            rslt = (rslt * (math.factorial(len(nbr[city])) %m)) %m
            if next_route != -1:
                city = next_route
                next_route = -1
                continue
            else:
                break
        if len(nbr[city]) > 1 and len(nbr[nbr[city][1]]) > 1:
            return 0
        rslt = (rslt * (math.factorial(len(nbr[city])-1) %m)) %m
        
        parent = city
        city = nbr[city][0]
        nbr[city].remove(parent)
        
    return rslt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        roads = []

        for _ in range(n - 1):
            roads.append(list(map(int, input().rstrip().split())))

        result = bytelandianTours(n, roads)

        fptr.write(str(result) + '\n')

    fptr.close()
