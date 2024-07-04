# #   https://www.hackerrank.com/challenges/largest-permutation/problem?isFullScreen=true

# You are given an unordered array of unique integers incrementing from . You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.

# Example


# The following arrays can be formed by swapping the  with the other elements:

# [2,1,3,4]
# [3,2,1,4]
# [4,2,3,1]
# The highest value of the four (including the original) is . If , we can swap to the highest possible value: .

# Function Description

# Complete the largestPermutation function in the editor below. It must return an array that represents the highest value permutation that can be formed.

# largestPermutation has the following parameter(s):

# int k: the maximum number of swaps
# int arr[n]: an array of integers
# Input Format

# The first line contains two space-separated integers  and , the length of  and the maximum swaps that can be performed. The second line contains  distinct space-separated integers from  to  as  where .

# Constraints



# Output Format

# Print the lexicographically largest permutation you can make with at most  swaps.
# Sample Input 0

# STDIN       Function
# -----       --------
# 5 1         n = 5, k = 1
# 4 2 3 5 1   arr = [4, 2, 3, 5, 1]
# Sample Output 0

# 5 2 3 4 1
# Explanation 0

# You can swap any two numbers in  and see the largest permutation is 

# Sample Input 1

# 3 1
# 2 1 3
# Sample Output 1

# 3 1 2
# Explanation 1

# With 1 swap we can get ,  and . Of these,  is the largest permutation.

# Sample Input 2

# 2 1
# 2 1
# Sample Output 2

# 2 1
# Explanation 2

# We can see that  is already the largest permutation. We don't make any swaps.

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    indices = {value: index for index, value in enumerate(arr)}
    n = len(arr)
    maxValue = n
    
    for i in range(n):
        if k == 0:
            break
        if arr[i] != maxValue:
            maxIndex = indices[maxValue]
            indices[arr[i]], indices[maxValue] = indices[maxValue], indices[arr[i]]
            arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
            k -= 1
        maxValue -= 1
        
    return arr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
