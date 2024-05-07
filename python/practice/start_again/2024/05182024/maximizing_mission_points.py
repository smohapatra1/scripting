# #   https://www.hackerrank.com/challenges/maximizing-mission-points/problem?isFullScreen=true

# Xander Cage has a list of cities he can visit on his new top-secret mission. He represents each city as a tuple of . The values of , , and  are distinct across all cities.

# We define a mission as a sequence of cities, , that he visits. We define the total  of such a mission to be the sum of the  of all the cities in his mission list.

# Being eccentric, he abides by the following rules on any mission:

# He can choose the number of cities he will visit (if any).
# He can start the mission from any city.
# He visits cities in order of strictly increasing .
# The absolute difference in  between adjacent visited cities in his mission must be at most .
# The absolute difference in  between adjacent visited cities in his mission must be at most .
# Given , , and the definitions for  cities, find and print the maximum possible total  that Xander can earn on a mission.

# Input Format

# The first line contains three space-separated integers describing the respective values of , , and .
# Each line  of the  subsequent lines contains four space-separated integers denoting the respective , , , and  for a city.

# Constraints

# Output Format

# Print a single integer denoting the maximum possible  that Xander can earn on a mission.

# Sample Input 0

# 3 1 1
# 1 1 1 3
# 2 2 2 -1
# 3 3 3 3
# Sample Output 0

# 5
# Explanation 0

# Xander can start at city , then go to city , and then go to city  for a maximum value of total 

# image

# Note that he cannot go directly from city  to city  as that would violate his rules that the absolute difference in  between adjacent visited cities be  and the absolute difference in  between adjacent visited cities be . Because  and , he cannot directly travel between those cities.



#!/bin/python3

import math
import os
import random
import re
import sys
from collections import namedtuple
from bisect import bisect_left

Place = namedtuple('Place', 'lat, long, height, points')

chunkplaces={} # places get inserted into lists contained here, grouped by keys of their locations
chunkvals={} # holds values

giant = False
def getkey(place, off_lat=0, off_long=0):
    return ((place.lat // d_lat + off_lat) * 200011) + place.long // d_long + off_long # unique for n<=200000

def recordvalue(place, val):
    if val < 0:
        return # not worth going here; no need to track
    key = getkey(place)
    if key not in chunkplaces:
        chunkplaces[key] = []
        chunkvals[key] = []
    if giant:
        if len(chunkvals[key]) == 0:
            chunkvals[key].append(-val)
            chunkplaces[key].append(place)
        else:
            if val < -chunkvals[key][0]:
                return
            else:
                chunkvals[key][0] = -val
                chunkplaces[key][0] = place
    else:
        i = bisect_left(chunkvals[key], -val)
        chunkplaces[key].insert(i, place)
        chunkvals[key].insert(i, -val)
        # print(i, val, [val for val in chunkvals[key]])

def getbestinchunk(place, key, best):
    # find best suitable match in chunk
    if key not in chunkvals:
        return 0
    for i, (cand, val) in enumerate(zip(chunkplaces[key], chunkvals[key])):
        # print("evaluating %s"%cand)
        if -val < best:
            # this is the best we have, but it's not as good as we've seen other places; abort
            return 0
        if abs(place.lat - cand.lat) <= d_lat \
            and abs(place.long - cand.long) <= d_long :
            # and cand.height > place.height: # height is given, assuming they're unique
            # suitable, return it
            return -val
    # no suitable match
    return 0
   
def getbest(place):
    # find best match in this and neighboring chunks, then pick the best
    best = 0 # always have the option to stop here
    for i in [0,1,-1]:
        for j in [0,1,-1]:
            key = getkey(place, i, j)
            ret = getbestinchunk(place, key, best)
            if ret > best:
                best = ret
    return best
    
def calculatevalue(place):
    val = place.points + getbest(place)
    recordvalue(place, val)
    return val


if __name__ == "__main__":
    n, d_lat, d_long = input().strip().split(' ')
    n, d_lat, d_long = [int(n), int(d_lat), int(d_long)]
    places = []
    if d_lat == 200000:
        giant = True
    for a0 in range(n):
        latitude, longitude, height, points = input().strip().split(' ')
        latitude, longitude, height, points = [int(latitude), int(longitude), int(height), int(points)]
        places.append(Place(latitude, longitude, height, points))
    places.sort(key=lambda p: -p.height) # compute highest first
    best = 0
    for p in places:
        ret = calculatevalue(p)
        if ret > best:
            best = ret
    print(best)



# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     d_lat = int(first_multiple_input[1])

#     d_long = int(first_multiple_input[2])

#     for n_itr in range(n):
#         second_multiple_input = input().rstrip().split()

#         latitude = int(second_multiple_input[0])

#         longitude = int(second_multiple_input[1])

#         height = int(second_multiple_input[2])

#         points = int(second_multiple_input[3])

        # Write your code here
