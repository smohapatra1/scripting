# #   https://www.hackerrank.com/challenges/bike-racers/problem?isFullScreen=true

# There are  bikers present in a city (shaped as a grid) having  bikes. All the bikers want to participate in the HackerRace competition, but unfortunately only  bikers can be accommodated in the race. Jack is organizing the HackerRace and wants to start the race as soon as possible. He can instruct any biker to move towards any bike in the city. In order to minimize the time to start the race, Jack instructs the bikers in such a way that the first  bikes are acquired in the minimum time.

# Every biker moves with a unit speed and one bike can be acquired by only one biker. A biker can proceed in any direction. Consider distance between bikes and bikers as Euclidean distance.

# Jack would like to know the square of required time to start the race as soon as possible.

# Input Format

# The first line contains three integers, , , and , separated by a single space.
# The following  lines will contain  pairs of integers denoting the co-ordinates of  bikers. Each pair of integers is separated by a single space. The next  lines will similarly denote the co-ordinates of the  bikes.

# Constraints




# ,  

# Output Format

# A single line containing the square of required time.

# Sample Input

# 3 3 2
# 0 1
# 0 2
# 0 3
# 100 1
# 200 2 
# 300 3
# Sample Output

# 40000
# Explanation

# There's need for two bikers for the race. The first biker (0,1) will be able to reach the first bike (100,1) in 100 time units. The second biker (0,2) will be able to reach the second bike (200,2) in 200 time units. This is the most optimal solution and will take 200 time units. So output will be 2002 = 40000.



#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'bikeRacers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY bikers
#  2. 2D_INTEGER_ARRAY bikes
#

debug = False

def show(matrix):
  if False:
    for row in matrix:
      print(str(row))

def cost(r,b):
  dx = b[0]-r[0]
  dy = b[1]-r[1]
  return dx*dx+dy*dy

def check(limit): # can we connect k riders to k bicycles with only segments less than limit?
  rtob = {r: [b for b in range(m) if c[r][b] <= limit] for r in range(n)}
  btor = {b: [r for r in range(m) if c[r][b] <= limit] for b in range(m)}
  # assign as many as we can, stop if we can get to k of them
  assd_r = {}
  assd_b = {}
  assd = 0
  arb = False
  assdnow = True
  while assdnow:
    if debug:
      print("Looping through")
    assdnow = False
    for r in range(n):
      if r not in assd_r:
        # node isn't assigned yet; try and find an augmenting path (DFS)
        # leads from this r to any unassigned b, possibly going through current assignations
        paths = deque() # contains candidate augmenting paths
        visited_r = set()
        visited_r.add(r)
        for b in reversed(rtob[r]):
          paths.append([(r,b)])
        while paths:
          path = paths.pop()
          rc, b = path[-1] # last tuple, try and expand from here
          # candidate: rc -> b
          if b not in assd_b:
            # b isn't assigned; this is an augmenting path
            if debug:
              print("assigning", path)
            for rc, b in path:
              assd_r[rc] = b
              assd_b[b] = rc
            assd += 1
            if assd >= k:
              if debug:
                print("Success! Assigned %d nodes of %d"%(assd,k))
              return True
            assdnow = True
            break # augmenting path found
          else: # b is assigned; follow the assigment back to an r (but not the same one) and try again
            if debug:
              print("continuing", path)
            rc = assd_b[b]
            if rc not in visited_r:
              visited_r.add(rc)
              for bc in reversed(rtob[rc]):
                if b != bc:
                  np = path[:]
                  np.append((rc,bc))
                  paths.append(np)
  if debug:
    print("Failure! Assigned %d nodes of %d"%(assd,k))
  return False

n,m,k = map(int,input().split())
rs = [tuple(map(int,input().split())) for _ in range(n)] # riders
bs = [tuple(map(int,input().split())) for _ in range(m)] # bicycles
c = [[cost(r,b) for b in bs] for r in rs] # adjacency graph - dense
show(c)
segs = sorted([c[r][b] for r in range(n) for b in range(m)])
# binary search using check function
lo = 0
hi = len(segs) - 1
while lo < hi:
  # invariant: smallest to succeed is x | lo <= x <= hi
  mid = (hi + lo) // 2
  if debug:
    print("examining (%d,%d,%d) (%d)"%(lo,mid,hi,segs[mid]))
  if check(segs[mid]):
    # succeeded, make mid highest in range (keep it since it might be target)
    hi = mid
  else:
    # failed, try more edges (mid can't be target)
    lo = mid + 1
# lo <- smallest to succeed
print(segs[lo])



# def bikeRacers(bikers, bikes):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     k = int(first_multiple_input[2])

#     bikers = []

#     for _ in range(n):
#         bikers.append(list(map(int, input().rstrip().split())))

#     bikes = []

#     for _ in range(n):
#         bikes.append(list(map(int, input().rstrip().split())))

#     result = bikeRacers(bikers, bikes)

#     fptr.write(str(result) + '\n')

#     fptr.close()
