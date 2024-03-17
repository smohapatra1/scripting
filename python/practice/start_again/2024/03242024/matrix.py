# https://www.hackerrank.com/challenges/matrix/problem
# The kingdom of Zion has cities connected by bidirectional roads. There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom. If two machines can join forces, they will attack. Neo has to destroy roads connecting cities with machines in order to stop them from joining forces. There must not be any path connecting two machines.

# Each of the roads takes an amount of time to destroy, and only one can be worked on at a time. Given a list of edges and times, determine the minimum time to stop the attack.

# For example, there are  cities called . Three of them have machines and are colored red. The time to destroy is shown next to each road. If we cut the two green roads, there are no paths between any two machines. The time required is .

# image
# Function Description

# Complete the function minTime in the editor below. It must return an integer representing the minimum time to cut off access between the machines.

# minTime has the following parameter(s):

# roads: a two-dimensional array of integers, each  where cities are connected by a road that takes  to destroy
# machines: an array of integers representing cities with machines
# Input Format

# The first line of the input contains two space-separated integers,  and , the number of cities and the number of machines.

# Each of the following  lines contains three space-separated integers, , and . There is a bidirectional road connecting  and , and to destroy this road it takes  units.

# Each of the last  lines contains an integer, , the label of a city with a machine.

# Constraints

# Output Format

# Return an integer representing the minimum time required to disrupt the connections among all machines.

# Sample Input

# 5 3
# 2 1 8
# 1 0 5
# 2 4 5
# 1 3 4
# 2
# 4
# 0
# Sample Output

# 10
# Explanation

# image

# The machines are located at the cities ,  and . Neo can destroy the green roads resulting in a time of . Destroying the road between cities  and  instead of between  and  would work, but it's not minimal.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY roads
#  2. INTEGER_ARRAY machines
#
class rec:
    def __init__(self, nodes, machine):
        self.nodes=set([nodes])
        self.machine = machine

def minTime(roads, machines):
    # Write your code here
    res = 0
    m = set(machines)
    d = dict ()
    r = sorted(roads, key=lambda x:x[2] , reverse=True)
    for a,b, w in r :
        d[a] = d.get(a, rec(a, a in m ))
        d[b] = d.get(b, rec(b, b in m ))
        s1 , s2 = d[a], d[b]
        if s1 == s2 :
            continue
        if s1.machine and s2.machine:
            res +=w 
            continue
        s1.nodes.update(s2.nodes)
        s1.machine = s1.machine or s2.machine 
        for c in s2.nodes:
            d[c] = s1
    return res    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()
