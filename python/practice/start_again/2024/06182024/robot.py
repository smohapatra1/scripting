# #   https://www.hackerrank.com/challenges/robot/problem?isFullScreen=true

# You have two arrays of integers,  and , where both have  number of elements. Consider the following function:

# score = 0

# int Go(step, energy) {
#     if (step == N) {
#         score += V[step];
#         return (score);
#     }
#     else {
#         int way = random(1, 2);
#         if (way == 1) {
#             score += V[step];
#         }
#         else {
#             energy = P[step];
#         }
#         if (energy > 0) {
#             Go(step + 1, energy - 1);
#         }
#         else {
#             KillTheWorld();
#         }
#     }
# }
# What is the maximum possible value of score that we can get in the end, if we call ?.
# Note that the function should never invoke KillTheWorld function. And  generates a random integer from set [1, 2].
# It is guaranteed there will be a solution that wont kill the world.

# Input Format

# The first line contains an integer N. Each of the following N lines contains a pair of integers. The i-th line contains a pair of numbers, , separated by space.

# Constraints




# Output Format

# Derive the maximum score given by return (score);.

# Sample Input

# 4
# 4 2
# 0 2
# 4 0
# 3 4
# Sample Output

# 7
# Explanation

# In the best case, the first and second function call in Go variable  will take value 2, while in the other calls it will be equal to 1 then the final score will be equal to the value of 7.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'robot' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY vp as parameter.
#

def best_total_score(config):
    N, V, P = config
    routes = [(0, 0)] 
    for step in range(1, N): 
        if not routes:
            print("all routes failed")
            return None
        this_score = V[step - 1]
        this_energy = P[step-1]
        
        if this_energy > 0:
            
            all_max_score = max([route_max_score for (energy, route_max_score) in routes])
            takeEnergy = (this_energy - 1, all_max_score)
            newRoutes = [(energy - 1, route_max_score + this_score) for (energy,  route_max_score) in routes if (energy > this_energy or (energy > 0 and route_max_score+this_score > all_max_score))]
            newRoutes.append(takeEnergy)
        else:
            newRoutes = [(energy - 1, route_max_score + this_score) for (energy, route_max_score) in routes if energy > 0]
        routes = newRoutes
    this_score = V[N - 1]
    return max(route_max_score for (energy, route_max_score) in routes) + this_score


def robot(vp):
    # Write your code here
    N = len(vp)
    V = []
    P = []
    for [vi, pi] in vp:
        V.append(vi)
        P.append(pi)
    config = (N,V,P)
    return best_total_score(config)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    vp = []

    for _ in range(n):
        vp.append(list(map(int, input().rstrip().split())))

    result = robot(vp)

    fptr.write(str(result) + '\n')

    fptr.close()
