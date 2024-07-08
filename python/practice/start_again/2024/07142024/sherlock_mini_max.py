# #   https://www.hackerrank.com/challenges/sherlock-and-minimax/problem?isFullScreen=true

# Watson gives Sherlock an array of integers. Given the endpoints of an integer range, for all  in that inclusive range, determine the minimum( abs(arr[i]-M) for all ) ). Once that has been determined for all integers in the range, return the  which generated the maximum of those values. If there are multiple 's that result in that value, return the lowest one.

# For example, your array  and your range is from  to  inclusive.

# M	|arr[1]-M|	|arr[2]-M|	|arr[3]-M|	|arr[4]-M|	Min
# 6	   3		   1		   1		   3		 1
# 7	   4		   2		   0		   2		 0
# 8	   5		   3		   1		   1		 1
# We look at the Min column and see the maximum of those three values is . Two 's result in that answer so we choose the lower value, .

# Function Description

# Complete the sherlockAndMinimax function in the editor below. It should return an integer as described.

# sherlockAndMinimax has the following parameters:
# - arr: an array of integers
# - p: an integer that represents the lowest value of the range for 
# - q: an integer that represents the highest value of the range for 

# Input Format

# The first line contains an integer , the number of elements in .
# The next line contains  space-separated integers .
# The third line contains two space-separated integers  and , the inclusive endpoints for the range of .

# Constraints




# Output Format

# Print the value of  on a line.

# Sample Input

# 3
# 5 8 14
# 4 9
# Sample Output

# 4
# Explanation


# M	|arr[1]-M|	|arr[2]-M|	|arr[3]-M|	Min
# 4	   1		   4		   10		 1
# 5	   0		   3		    9		 0
# 6	   1		   2		    8		 1
# 7	   2		   1		    7		 1
# 8	   3		   0		    6		 0
# 9	   4		   1		    5		 1
# For , or , the result is . Since we have to output the smallest of the multiple solutions, we print .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndMinimax' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER p
#  3. INTEGER q
#

def sherlockAndMinimax(arr, p, q):
    # Write your code here
    arr.sort()
    diff = -float('inf')
    ans = 0 
    if p < arr[0]:
        diff = arr[0] - p 
        ans = p
    n = len(arr)
    for i in range(1, n ):
        x = min(q, (arr[i] + arr[i-1])//2)
        x = max(p, x)
        diff1 = arr[i] - x 
        diff2 = x - arr[i-1]
        y = min(diff1, diff2)
        if y > diff:
            if diff2 == y:
                diff = diff2
                ans = x 
            else:
                diff = diff1
                ans = x 
    if arr[-1] < q :
        x = q - arr[-1]
        if x > diff:
            ans = q 
    return ans
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()
