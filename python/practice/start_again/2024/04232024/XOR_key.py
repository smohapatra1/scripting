# #   https://www.hackerrank.com/challenges/xor-key/problem?isFullScreen=true

# Xorq has invented an encryption algorithm which uses bitwise XOR operations extensively. This encryption algorithm uses a sequence of non-negative integers  as its key. To implement this algorithm efficiently, Xorq needs to find maximum value of  for given integers ,  and , such that, . Help Xorq implement this function.

# For example, , ,  and . We test each  for all values of  between  and  inclusive:

# j   x[j]    x[j]^4
# 1   3       7
# 2   5       1
# 3   9       13
# Our maximum value is .

# Function Description

# Complete the xorKey function in the editor below. It should return an integer array where each value is the response to a query.

# xorKey has the following parameters:

# x: a list of integers
# queries: a two dimensional array where each element is an integer array that consists of  for the  query at indices  and  respectively.
# Input Format

# The first line contains an integer , the number of test cases.
# The first line of each test case contains two space-separated integers  and , the size of the integer array  and the number of queries against the test case.
# The next line contains  space-separated integers .
# Each of next  lines describes a query which consists of three integers  and .

# Constraints





# Output Format

# For each query, print the maximum value for , such that,  on a new line.

# Sample Input 0

# 1
# 15 8
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 10 6 10
# 1023 7 7
# 33 5 8
# 182 5 10
# 181 1 13
# 5 10 15
# 99 8 9
# 33 10 14
# Sample Output 0

# 13
# 1016
# 41
# 191
# 191
# 15
# 107
# 47
# Explanation 0

# First Query (10 6 10): . The maximum is .

# Second Query (1023 7 7): 

# Third Query (33 5 8): 

# Fourth Query (182 5 10): 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xorKey' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY x
#  2. 2D_LONG_INTEGER_ARRAY queries
#

def xorKey(x, queries):
    # Write your code here
    # Solution - 01 
    # res=[]
    # for i in queries:
    #     maxi=0
    #     a,l,r=i[0],i[1],i[2]
    #     if l==r :
    #         maxi=a^x[l-1]
    #     else :
    #         for j in range(l,r+1):
    #             if j<=len(x):
    #                 xori=a^x[j-1]
    #                 if xori>=maxi : 
    #                     maxi=xori 
    #     res.append(maxi)
    # return res
    
    # Solution - 02
    lst=[]
    for j in queries:
        a,l,r=j
        y=filter(lambda i:l<=i and i<=r,x)
        res=set([a^k for k in y])
        lst.append(max(res))
    return lst
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        q = int(first_multiple_input[1])

        x = list(map(int, input().rstrip().split()))

        queries = []

        for _ in range(q):
            queries.append(list(map(int, input().rstrip().split())))

        result = xorKey(x, queries)

        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
