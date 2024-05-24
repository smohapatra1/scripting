# #   https://www.hackerrank.com/challenges/counting-special-sub-cubes/problem?isFullScreen=true

# Given an  cube, let  (where ) denote the value stored in cell .

# A  sub-cube (where ) of an  cube is considered to be special if the maximum value stored in any cell in the sub-cube is equal to .

# For each  in the inclusive range , calculate the number of special sub-cubes. Then print each  as a single line of space-separated integers (i.e., ).

# Input Format

# The first line contains an integer, , denoting the number of queries. The  subsequent lines describe each query over two lines:

# The first line contains an integer, , denoting the side length of the initial cube.
# The second line contains  space-separated integers describing an array of  integers in the form . The integer in some cell  is calculated using the formula .
# Constraints

#  where 
# Output Format

# For each query, print  space-separated integers where the  integer denotes the number of special sub-cubes for .

# Sample Input

# 2
# 2
# 2 1 1 1 1 1 1 1
# 2
# 1 1 1 1 2 1 1 2
# Sample Output

# 7 1
# 6 1
# Explanation

# We must perform the following  queries:

# We have a cube of size  and must calculate the number of special sub-cubes for the following values of :

# : There are  sub-cubes of size  and seven of them have a maximum value of  written inside them. So, for , the answer is .
# : There is only one sub-cube of size  and the maximum number written inside it is . So, for , the answer is .
# We then print the respective values for each  as a single line of space-separated integers (i.e., 7 1).

# We have a cube of size  and must calculate the number of special sub-cubes for the following values of :

# : There are  sub-cubes of size  and six of them have a maximum value of  written inside them. So, for , the answer is .
# : There is only one sub-cube of size  and the maximum number written inside it is . So, for , the answer is .
# We then print the respective values for each  as a single line of space-separated integers (i.e., 6 1).


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'specialSubCubes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY cube as parameter.
#

def findMax(arr, s, indices, n):
    largest = 1
    for i in indices:
        cur = arr[s+i]
        if cur > largest:
            largest = cur
        elif cur == n:
            largest = n
            break
    return largest

def findSpecial(arr, k, n):
    temp = arr
    if k > 1:
        temp = []
        m = n - k + 2
        m2 = m*m
        indices = [0, 1, m, m+1, m2, m2+1, m2+m, m2+m+1]
        for i in range(m-1):
            start = m2*i
            for j in range(m-1):
                for z in range(m-1):
                    largest = findMax(arr, start, indices, n)
                    temp.append(largest)
                    start += 1
                start += 1
    return temp    
               
q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    for k in range(1, n+1):
        arr = findSpecial(arr, k, n)
        print(arr.count(k), end=' ')
    print('')
    
# def specialSubCubes(cube):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         cube = list(map(int, input().rstrip().split()))

#         result = specialSubCubes(cube)

#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')

#     fptr.close()
