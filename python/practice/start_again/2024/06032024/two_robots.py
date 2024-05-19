# #   https://www.hackerrank.com/challenges/two-robots/problem?isFullScreen=true

# You have a warehouse with  containers filled with an infinite number of candies. The containers are arranged in a single row, equally spaced to be  meter apart. You also have  robots that can pick up  piece of candy and transport it between any two containers.

# The robots take instructions in the form of queries consisting of two integers,  and , respectively. To execute a query, a robot travels to container , picks up  candy, transports it to container , and then stops at  until it receives another query.

# Calculate the minimum total distance the robots must travel to execute  queries in order.

# Note: You choose which robot executes each query.

# Input Format

# The first line contains a single integer,  (the number of test cases); each of the  test cases is described over  lines.

# The first line of a test case has two space-separated integers,  (the number of containers) and  (the number of queries).
# The  subsequent lines each contain two space-separated integers,  and , respectively; each line  describes the  query.

# Constraints

# Output Format

# On a new line for each test case, print an integer denoting the minimum total distance that the robots must travel to execute the queries in order.

# Sample Input

# 3
# 5 4
# 1 5
# 3 2
# 4 1
# 2 4
# 4 2
# 1 2
# 4 3
# 10 3
# 2 4
# 5 4
# 9 8
# Sample Output

# 11
# 2
# 5
# Explanation

# In this explanation, we refer to the two robots as  and , each container  as , and the total distance traveled for each query  as .

# Note: For the first query a robot executes, there is no travel distance. For each subsequent query that robot executes, it must travel from the location where it completed its last query.

# Test Case 0:
# The minimum distance traveled is :

# Robot: 

#  meters.
# Robot: 

#  meter.
# Robot: 

#  meters.
# Robot: 

#  meters.
# Sum the distances traveled () and print the result on a new line.

# Test Case 1:

# Robot: 

#  meters.
# Robot: 

#  meters.
# Sum the distances traveled () and print the result on a new line.

# Test Case 2:

# Robot: 

#  meters.
# Robot: 

#  meters.
# Robot: 

#  meters.
# Sum the distances traveled () and print the result on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoRobots' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. 2D_INTEGER_ARRAY queries
#

from collections import defaultdict

def dist(x, y):
    return abs(x - y)

def solve(boxes):
    boxes.reverse()
    c = [0] * len(boxes)
    c[0] = dist(boxes[0][0], boxes[0][1])
    for bi in range(1, len(boxes)):
        bx, by = boxes[bi]
        cur_dist = dist(bx, by)
        dist_to_prev = dist(by, boxes[bi - 1][0])
        c[bi] = c[bi - 1] + dist_to_prev + cur_dist
        for i in range(0, bi-1):
            c[bi - 1] = min(c[bi - 1], dist(by, boxes[i][0]) + c[i])
            c[i] += dist_to_prev + cur_dist

        c[bi - 1] += cur_dist

    return min(c)


t = int(input())

for i in range(0, t):
    m, n = map(int, input().strip().split(' '))
    boxes = []
    for i in range(0, n):
        boxes.append([int(x) for x in input().strip().split(' ')])
        
    print(solve(boxes))

# def twoRobots(m, queries):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     first_multiple_input = input().rstrip().split()

#     m = int(first_multiple_input[0])

#     n = int(first_multiple_input[1])

#     queries = []

#     for _ in range(n):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = twoRobots(m, queries)

#     fptr.write(str(result) + '\n')

#     fptr.close()
