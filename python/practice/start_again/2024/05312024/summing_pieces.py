# #   https://www.hackerrank.com/challenges/summing-pieces/problem?isFullScreen=true

# Consider an array, , of length . We can split  into contiguous segments called pieces and store them as another array, . For example, if , we have the following arrays of pieces:

#  contains three -element pieces.
#  contains two pieces, one having  elements and the other having  element.
#  contains two pieces, one having  element and the other having  elements.
#  contains one -element piece.
# We consider the value of a piece in some array  to be , and we consider the total value of some array  to be the sum of the values for all pieces in that . For example, the total value of  is .

# Given , find the total values for all possible 's, sum them together, and print this sum modulo  on a new line.

# Input Format

# The first line contains a single integer, , denoting the size of array .
# The second line contains  space-separated integers describing the respective values in  (i.e., ).

# Constraints

# Output Format

# Print a single integer denoting the sum of the total values for all piece arrays ('s) of , modulo .

# Sample Input 0

# 3
# 1 3 6
# Sample Output 0

# 73
# Explanation 0
# Given , our piece arrays are:

# , and .
# , and .
# , and .
# , and .
# When we sum all the total values, we get . Thus, we print the result of  on a new line.

# Sample Input 1

# 5
# 4 2 9 10 1
# Sample Output 1

# 971


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingPieces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def summingPieces(arr):
    # Write your code here
    mod = 10 ** 9 + 7 
    n = len(arr)
    c = (pow(2, n, mod) - 1 ) % mod
    v = (arr[0] * c ) % mod
    for i in range(2, n+1):
        c = ( c + pow(2, n-i, mod) - pow(2, i-2 , mod)) % mod 
        v = ( v + arr[i-1] * c ) % mod 
    return v
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
