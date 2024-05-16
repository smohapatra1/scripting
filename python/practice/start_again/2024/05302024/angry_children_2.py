# #   https://www.hackerrank.com/challenges/angry-children-2/problem?isFullScreen=true

# Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has brought a box of packets of candies and would like to distribute one packet to each of the children. Each of the packets contains a number of candies. He wants to minimize the cumulative difference in the number of candies in the packets he hands out. This is called the unfairness sum. Determine the minimum unfairness sum achievable.

# For example, he brings  packets where the number of candies is . There are  children. The minimum difference between all packets can be had with  from indices  and . We must get the difference in the following pairs: . We calculate the unfairness sum as:

# packets candies				
# 0	3		indices		difference	result
# 1	3		(0,1),(0,2)	|3-3| + |3-4|	1 
# 2	4		(1,2)		|3-4|		1

# Total = 2
# Function Description

# Complete the angryChildren function in the editor below. It should return an integer that represents the minimum unfairness sum achievable.

# angryChildren has the following parameter(s):

# k: an integer that represents the number of children
# packets: an array of integers that represent the number of candies in each packet
# Input Format

# The first line contains an integer .
# The second line contains an integer .
# Each of the next  lines contains an integer .

# Constraints




# Output Format

# A single integer representing the minimum achievable unfairness sum.

# Sample Input 0

# 7
# 3
# 10
# 100
# 300
# 200
# 1000
# 20
# 30
# Sample Output 0

# 40
# Explanation 0

# Bill Gates will choose packets having 10, 20 and 30 candies. The unfairness sum is .

# Sample Input 1

# 10
# 4
# 1
# 2
# 3
# 4
# 10
# 20
# 30
# 40
# 100
# 200
# Sample Output 1

# 10
# Explanation 1

# Bill Gates will choose 4 packets having 1,2,3 and 4 candies. The unfairness sum i .



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryChildren' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY packets
#

def angryChildren(k, packets):
    # Write your code here
    packets.sort()
    n = len(packets)
    s = -packets[0]
    d = 0
    for i in range(k):
        s += packets[i]
        d += (2*i-k+1)*packets[i]
    ans = d
    for shift in range(1,n-k):
        d += (- 2*s + (k-1)*(packets[shift-1]+packets[shift+k-1]))
        s += (packets[shift+k-1]-packets[shift])
        ans = min(ans,d)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    packets = []

    for _ in range(n):
        packets_item = int(input().strip())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
