# #   https://www.hackerrank.com/challenges/fibonacci-modified/problem?isFullScreen=true

# Implement a modified Fibonacci sequence using the following definition:

# Given terms  and  where , term  is computed as:

# Given three integers, , , and , compute and print the  term of a modified Fibonacci sequence.

# Example



# Return .

# Function Description

# Complete the fibonacciModified function in the editor below. It must return the  number in the sequence.

# fibonacciModified has the following parameter(s):

# int t1: an integer
# int t2: an integer
# int n: the iteration to report
# Returns

# int: the  number in the sequence
# Note: The value of  may far exceed the range of a -bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to compensate for the size of the result.

# Input Format

# A single line of three space-separated integers, the values of , , and .

# Constraints

#  may far exceed the range of a -bit integer.
# Sample Input

# 0 1 5
# Sample Output

# 5
# Explanation

# The first two terms of the sequence are  and , which gives us a modified Fibonacci sequence of . The  term is .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    # Write your code here
    if n == 1 :
        return t1
    elif n == 2:
        return t2
    else:
        data = [0]*n
        data[0] = t1 
        data[1] = t2
        for i in range(2, n ):
            data[i] = data[i-2] + data[i-1]** 2
        return data[-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
