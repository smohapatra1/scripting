# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-jesse-and-cookies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four

# Jesse loves cookies and wants the sweetness of some cookies to be greater than value . To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

# sweetness  Least sweet cookie   2nd least sweet cookie).

# This occurs until all the cookies have a sweetness .

# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .

# Example


# The smallest values are .
# Remove them then return  to the array. Now .
# Remove  and return  to the array. Now .
# Remove , return  and .
# Finally, remove  and return  to . Now .
# All values are  so the process stops after  iterations. Return .

# Function Description
# Complete the cookies function in the editor below.

# cookies has the following parameters:

# int k: the threshold value
# int A[n]: an array of sweetness values
# Returns

# int: the number of iterations required or 
# Input Format

# The first line has two space-separated integers,  and , the size of  and the minimum required sweetness respectively.

# The next line contains  space-separated integers, .

# Constraints




# Sample Input

# STDIN               Function
# -----               --------
# 6 7                 A[] size n = 6, k = 7
# 1 2 3 9 10 12       A = [1, 2, 3, 9, 10, 12]  
# Sample Output

# 2
# Explanation

# Combine the first two cookies to create a cookie with sweetness  = 
# After this operation, the cookies are .
# Then, combine the cookies with sweetness  and sweetness , to create a cookie with resulting sweetness  = 
# Now, the cookies are .
# All the cookies have a sweetness .

# Thus,  operations are required to increase the sweetness.



#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    h=[i for i in A]
    heapq.heapify(h)
    ans=0
    while h[0] <k and len(h) > 1:
        f=heapq.heappop(h)
        s=heapq.heappop(h)
        heapq.heappush(h, f+2*s)
        ans+=1
    if h[0] >=k:
        return ans
    else:
        return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
