# #   https://www.hackerrank.com/challenges/string-reduction/problem?isFullScreen=true

# Given a string consisting of the letters ,  and , we can perform the following operation:

# Take any two adjacent distinct characters and replace them with the third character.
# Find the shortest string obtainable through applying this operation repeatedly.

# For example, given the string  we can reduce it to a  character string by replacing  with  and  with : .

# Function Description

# Complete the stringReduction function in the editor below. It must return an integer that denotes the length of the shortest string obtainable.

# stringReduction has the following parameter:
# - s: a string

# Input Format

# The first line contains the number of test cases .

# Each of the next  lines contains a string  to process.

# Constraints

# Output Format

# For each test case, print the length of the resultant minimal string on a new line.

# Sample Input

# 3  
# cab  
# bcab  
# ccccc
# Sample Output

# 2  
# 1  
# 5
# Explanation

# For the first case, there are two solutions:  or .
# For the second case, one optimal solution is: .
# For the third case, no operations can be performed so the answer is .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringReduction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringReduction(s):
    # Write your code here
    c = [s.count(chr(i)) % 2 for i in range(97, 100)]
    return (1, 2)[sum(c) in (0, 3)] if len(set(s)) !=1 else len(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
