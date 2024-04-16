# #   https://www.hackerrank.com/challenges/iterate-it/problem?isFullScreen=true

# Consider the following pseudocode, run on an array  of length :

# rep := 0
# while A not empty:
#     B := []
#     for x in A, y in A:
#         if x != y: append absolute_value(x - y) to B
#     A := B
#     rep := rep + 1
# Given the values of  and array , compute and print the final value of  after the pseudocode above terminates; if the loop will never terminate, print -1 instead.

# Input Format

# The first line contains a single integer, , denoting the length of array .
# The second line contains  space-separated integers describing the respective values of .

# Constraints

# Output Format

# Print the final value of  after the pseudocode terminates; if the loop will never terminate, print -1 instead.

# Sample Input 0

# 3
# 1 3 4
# Sample Output 0

# 4
# Explanation 0

# After the first loop,  becomes . After the second loop, the array only contains 's and 's. After the third loop, the array only contains 's. After the fourth loop, the array is empty. Because the value of  is incremented after each loop,  at the time the loop terminates. Thus, we print 4 as our answer.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'iterateIt' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def iterateIt(a):
    # Write your code here
    s = 0
    for i in a:
        s |= (1 << (i - 1))

    for i in range(s.bit_length() + 1):

        smallest = (s ^ (s - 1)).bit_length()
        s1 = s >> smallest
        if s1 | s == s:
            return i + s.bit_length() // smallest
        t = s1
        s = s1
        while s != 0:
            smallest = (s ^ (s - 1)).bit_length()
            s1 = s >> smallest
            t |= s1
            if s1 | s == s:
                break
            s = s1
        s = t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = iterateIt(a)

    fptr.write(str(result) + '\n')

    fptr.close()
