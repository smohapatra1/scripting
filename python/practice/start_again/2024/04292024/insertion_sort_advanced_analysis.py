# #   https://www.hackerrank.com/challenges/insertion-sort/problem?isFullScreen=true

# Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of shifts an insertion sort performs when sorting an array?

# If  is the number of elements over which the  element of the array has to shift, then the total number of shifts will be  ... + .

# Example

# Array		Shifts
# [4,3,2,1]	
# [3,4,2,1]	1
# [2,3,4,1]	2
# [1,2,3,4]	3

# Total shifts = 1 + 2 + 3 = 6
# Function description

# Complete the insertionSort function in the editor below.

# insertionSort has the following parameter(s):

# int arr[n]: an array of integers
# Returns
# - int: the number of shifts required to sort the array

# Input Format

# The first line contains a single integer , the number of queries to perform.

# The following  pairs of lines are as follows:

# The first line contains an integer , the length of .
# The second line contains  space-separated integers .
# Constraints

# Sample Input

# 2  
# 5  
# 1 1 1 2 2  
# 5  
# 2 1 3 1 2
# Sample Output

# 0  
# 4   
# Explanation

# The first query is already sorted, so there is no need to shift any elements. In the second case, it will proceed in the following way.

# Array: 2 1 3 1 2 -> 1 2 3 1 2 -> 1 1 2 3 2 -> 1 1 2 2 3
# Moves:   -        1       -    2         -  1            = 4




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def merge(list1, list2, counter):
    combined = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            counter += len(list1) - i
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined, counter
    
def divideAndConquer(arr):
    if len(arr) == 1:
        return arr, 0
        
    mid_index = len(arr) // 2
    
    left = divideAndConquer(arr[:mid_index])
    right = divideAndConquer(arr[mid_index:])
    
    return merge(left[0], right[0], left[1] + right[1])
    

def insertionSort(arr):
    # Write your code here
    return divideAndConquer(arr)[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
