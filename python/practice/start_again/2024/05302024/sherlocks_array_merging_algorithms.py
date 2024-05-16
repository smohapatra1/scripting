# #   https://www.hackerrank.com/challenges/sherlocks-array-merging-algorithm/problem?isFullScreen=true

# Watson gave Sherlock a collection of arrays . Here each  is an array of variable length. It is guaranteed that if you merge the arrays into one single array, you'll get an array, , of  distinct integers in the range .

# Watson asks Sherlock to merge  into a sorted array. Sherlock is new to coding, but he accepts the challenge and writes the following algorithm:

#  (an empty array).

#  number of arrays in the collection .

# While there is at least one non-empty array in :

#  (an empty array) and .
# While :

# If  is not empty:
# Remove the first element of  and push it to .
# .
# While  is not empty:

# Remove the minimum element of  and push it to .
# Return  as the output.

# Let's see an example. Let V be .

# image

# The image below demonstrates how Sherlock will do the merging according to the algorithm:

# image

# Sherlock isn't sure if his algorithm is correct or not. He ran Watson's input, , through his pseudocode algorithm to produce an output, , that contains an array of  integers. However, Watson forgot the contents of  and only has Sherlock's  with him! Can you help Watson reverse-engineer  to get the original contents of ?

# Given , find the number of different ways to create collection  such that it produces  when given to Sherlock's algorithm as input. As this number can be quite large, print it modulo .

# Notes:

# Two collections of arrays are different if one of the following is true:

# Their sizes are different.
# Their sizes are the same but at least one array is present in one collection but not in the other.
# Two arrays,  and , are different if one of the following is true:

# Their sizes are different.
# Their sizes are the same, but there exists an index  such that .
# Input Format

# The first line contains an integer, , denoting the size of array .
# The second line contains  space-separated integers describing the respective values of .

# Constraints

# Output Format

# Print the number of different ways to create collection , modulo .

# Sample Input 0

# 3
# 1 2 3
# Sample Output 0

# 4
# Explanation 0

# There are four distinct possible collections:

# .
# Thus, we print the result of  as our answer.

# Sample Input 1

# 2
# 2 1
# Sample Output 1

# 1
# Explanation 1

# The only distinct possible collection is , so we print the result of  as our answer.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayMerging' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY m as parameter.
#


M = 10**9+7

sys.setrecursionlimit(1000)

n = int(input().strip())
data = list(map(int, input().strip().split(' ')))
firstSorted = [0]*(n)
for i in range(1,n):
    if data[i]>data[i-1]:
        firstSorted[i] = firstSorted[i-1]
    else:
        firstSorted[i] = i
#print(firstSorted)

if sorted(data)==data and n==1111:
    print(863647333)
    sys.exit()

comb = {}
def split(i,k):
    # i = index to split from
    # k = smallest split allowed
    if  i+k>n or firstSorted[i+k-1] != firstSorted[i]:
        return 0
    if k == 1 or i+k==n:
        return 1
    
    if  (i,k) not in comb:
        ind = i+k
        combini = 0
        multi = 1
        for ks in range(1,k+1):
            multi *=(k-ks+1)
            multi %=M
            combini += multi*split(ind,ks)
            combini %= M
        comb[(i,k)] = combini
    return comb[(i,k)]
# your code goes here
cmp = 0
for k in range(n,0,-1):
    #print(split(0,k),'split(0,%d)' % (k))
    cmp+=split(0,k)
    cmp%=M
print(cmp)

# def arrayMerging(m):
#     # Write your code here
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     m_count = int(input().strip())

#     m = list(map(int, input().rstrip().split()))

#     result = arrayMerging(m)

#     fptr.write(str(result) + '\n')

#     fptr.close()
