# #   https://www.hackerrank.com/challenges/cloudy-day/problem?isFullScreen=true

# Quibdó in Colombia is one among the cities that receive maximum rainfall in the world.

# All year round, the city is covered in clouds. The city has many towns, located on a one-dimensional line. The positions and populations of each town on the number line are known to you. Every cloud covers all towns located at a certain distance from it. A town is said to be in darkness if there exists at least one cloud such that the town is within the cloud's range. Otherwise, it is said to be sunny.

# image

# The city council has determined that they have enough money to remove exactly one cloud using their latest technology. Thus they want to remove the cloud such that the fewest number of people are left in darkness after the cloud is removed. What is the maximum number of people that will be in a sunny town after removing exactly one cloud?

# Note: If a town is not covered by any clouds, then it is already considered to be sunny, and the population of this town must also be included in the final answer.

# Complete the function maximumPeople which takes four arrays representing the populations of each town, locations of the towns, locations of the clouds, and the extents of coverage of the clouds respectively, and returns the maximum number of people that will be in a sunny town after removing exactly one cloud.

# Input Format

# The first line of input contains a single integer , the number of towns.

# The next line contains  space-separated integers . The  integer in this line denotes the population of the  town.

# The next line contains  space-separated integers  denoting the location of the  town on the one-dimensional line.

# The next line consists of a single integer  denoting the number of clouds covering the city.

# The next line contains  space-separated integers  the  of which denotes the location of the  cloud on the coordinate axis.

# The next line consists of  space-separated integers  denoting the range of the  cloud.

# Note: The range of each cloud is computed according to its location, i.e., the  cloud is located at position  and it covers every town within a distance of  from it. In other words, the  cloud covers every town with location in the range .

# Constraints

# Output Format

# Print a single integer denoting the maximum number of people that will be in a sunny town by removing exactly one cloud.

# Sample Input 0

# 2
# 10 100
# 5 100
# 1
# 4
# 1
# Sample Output 0

# 110
# Explanation 0

# In the sample case, there is only one cloud which covers the first town. Our only choice is to remove this sole cloud which will make all towns sunny, and thus, all  people will live in a sunny town.

# image

# As you can see, the only cloud present, is at location  on the number line and has a range , so it covers towns located at ,  and  on the number line. Hence, the first town is covered by this cloud and removing this cloud makes all towns sunny.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    x, p = zip(*sorted(zip(x, p )))
    not_visited = [ i for i in range(len(y))]
    not_visited.sort(key = lambda x:y[x] - r[x])
    to_visit = []
    sum_sunny = dict()
    max_pop = sum(p)
    cloud_pop = [0]* len(y)
    idx_x = 0 
    while idx_x < len(x):
        pos = x[idx_x]
        population = p[idx_x]
        j = 0 
        while j < len(not_visited):
            element = not_visited[j]
            if y[element] - r[element] <= pos:
                to_visit.append((element, y[element]+r[element]))
                del not_visited[j]
            else:
                break
        j = 0 
        to_check = None
        while j < len(to_visit):
            element, max_pos = to_visit[j]
            if max_pos - pos >= 0:
                to_check=element
                if idx_x not in sum_sunny:
                    sum_sunny[idx_x]=population
                else:
                    to_check=None 
                    break
                j+=1
            else:
                del to_visit[j]
                
        idx_x+=1
        if to_check is not None:
            cloud_pop[to_check]+=population
        
    for pop in sum_sunny.values():
            max_pop-=pop
            
    return max(cloud_pop) + max_pop 
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
