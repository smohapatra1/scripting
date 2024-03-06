# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-equal-stacks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four

# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

# Example




# There are  and  cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from  (heights = [1, 2]) and from  (heights = [1, 1]) so that the three stacks all are 2 units tall. Return  as the answer.

# Note: An empty stack is still a stack.

# Function Description

# Complete the equalStacks function in the editor below.

# equalStacks has the following parameters:

# int h1[n1]: the first array of heights
# int h2[n2]: the second array of heights
# int h3[n3]: the third array of heights
# Returns

# int: the height of the stacks when they are equalized
# Input Format

# The first line contains three space-separated integers, , , and , the numbers of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

# The second line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
# The third line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
# The fourth line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
# Constraints

# Sample Input

# STDIN       Function
# -----       --------
# 5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
# 3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
# 4 3 2       h2 = [4, 3, 2]
# 1 1 4 1     h3 = [1, 1, 4, 1]
# Sample Output

# 5
# Explanation

# Initially, the stacks look like this:

# initial stacks

# To equalize thier heights, remove the first cylinder from stacks  and , and then remove the top two cylinders from stack  (shown below).

# modified stacks

# The stack heights are reduced as follows:

# All three stacks now have , the value to return.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    s1,s2,s3=sum(h1),sum(h2),sum(h3)
    while s1!=s2 or s2!=s3:
        if s1>s2 or s1>s3:
            s1-=h1.pop(0)
        elif s2>s1 or s2>s3:
            s2-=h2.pop(0)
        else:
            s3-=h3.pop(0)
    return(s1) 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print (result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
