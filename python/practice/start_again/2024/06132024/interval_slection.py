# #   https://www.hackerrank.com/challenges/interval-selection/problem?isFullScreen=true

# Given a set of  intervals, find the size of its largest possible subset of intervals such that no three intervals in the subset share a common point.

# Input Format

# The first line contains an integer, , denoting the number of interval sets you must find answers for. The  subsequent lines describe each of the  interval sets as follows:

# The first line contains an integer, , denoting the number of intervals in the list.
# Each line  of the  subsequent lines contains two space-separated integers describing the respective starting () and ending () boundaries of an interval.
# Constraints

# Output Format

# For each of the  interval sets, print an integer denoting the size of the largest possible subset of intervals in the given set such that no three points in the subset overlap.

# Sample Input

# 4
# 3
# 1 2
# 2 3
# 2 4
# 3
# 1 5
# 1 5
# 1 5
# 4
# 1 10
# 1 3
# 4 6
# 7 10
# 4
# 1 10
# 1 3
# 3 6
# 7 10
# Sample Output

# 2
# 2
# 4
# 3
# Explanation

# For set , all three intervals fall on point  so we can only choose any  of the intervals. Thus, we print  on a new line.

# For set , all three intervals span the range from  to  so we can only choose any  of them. Thus, we print  on a new line.

# For set , we can choose all  intervals without having more than two of them overlap at any given point. Thus, we print  on a new line.

# For set , the intervals , , and  all overlap at point , so we must only choose  of these intervals to combine with the last interval, , for a total of  qualifying intervals. Thus, we print  on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'intervalSelection' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def intervalSelection(intervals):
    # Write your code here
    intervals.sort(key = lambda x : x[1])
    noOfSelections = 0
    busy = [[0, 0], [0, 0]]
    for interval in intervals:
        if interval[0] > busy[1][1]:
            noOfSelections += 1
            busy[1] = interval
        else: 
            if interval[0] > busy[0][1]:
                noOfSelections += 1
                busy[0] = interval
                if interval[1] > busy[1][1]:
                    (busy[0], busy[1]) = (busy[1], busy[0])
    return noOfSelections

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        intervals = []

        for _ in range(n):
            intervals.append(list(map(int, input().rstrip().split())))

        result = intervalSelection(intervals)

        fptr.write(str(result) + '\n')

    fptr.close()
