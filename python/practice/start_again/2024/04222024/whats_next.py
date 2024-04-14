# #   https://www.hackerrank.com/challenges/whats-next/problem?isFullScreen=true


# Johnny is playing with a large binary number, . The number is so large that it needs to be compressed into an array of integers, , where the values in even indices () represent some number of consecutive  bits and the values in odd indices () represent some number of consecutive  bits in alternating substrings of .

# For example, suppose we have array .  represents ,  represents ,  represents ,  represents , and  represents . The number of consecutive binary characters in the  substring of  corresponds to integer , as shown in this diagram:

# whats.png

# When we assemble the sequential alternating sequences of 's and 's, we get .

# We define setCount() to be the number of 's in a binary number, . Johnny wants to find a binary number, , that is the smallest binary number  where setCount() = setCount(). He then wants to compress  into an array of integers,  (in the same way that integer array  contains the compressed form of binary string ).

# Johnny isn't sure how to solve the problem. Given array , find integer array  and print its length on a new line. Then print the elements of array  as a single line of space-separated integers.

# Input Format

# The first line contains a single positive integer, , denoting the number of test cases. Each of the  subsequent lines describes a test case over  lines:

# The first line contains a single positive integer, , denoting the length of array .
# The second line contains  positive space-separated integers describing the respective elements in integer array  (i.e., ).
# Constraints

# Subtasks

# For a  score, .
# For a  score, .
# Output Format

# For each test case, print the following  lines:

# Print the length of integer array  (the array representing the compressed form of binary integer ) on a new line.
# Print each element of  as a single line of space-separated integers.
# It is guaranteed that a solution exists.

# Sample Input 0

# 1
# 5
# 4 1 3 2 4
# Sample Output 0

# 7
# 4 1 3 1 1 1 3
# Explanation 0

# , which expands to . We then find setCount() . The smallest binary number  which also has eleven 's is . This can be reduced to the integer array . This is demonstrated by the following figure:

# whats-2.png

# Having found , we print its length () as our first line of output, followed by the space-separated elements in  as our second line of output.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatsNext' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def whatsNext(arr):
    # Write your code here
    l = len(arr) -1
    # case: l == 0
    if not l:
        if arr[0] == 1:
            print(2)
            print(*[1, 1])
        else:
            print(3)
            print(*[1, 1, arr[0]-1])
        return
    # find index for least significant set bit
    i = l-1 if l & 1 else l
    # case: l == 1
    if l == 1:
        t = [1, arr[1] +1, arr[0] -1]
    # case: last bit group is off
    elif l - i:
        t = arr[:i-1] + [arr[i-1] -1, 1, arr[-1] + 1, arr[i] -1]
    # case: last bit group is set
    else:
        t = arr[:i-1] + [arr[i-1] -1, 1, 1, arr[i] -1]
    # handle zeros
    if not t[-1]: t.pop(-1)
    if t.count(0):
        i_lst = []
        for i,a in enumerate(t):
            if not a:
                #  combine bits around zero
                t[i-1] += t[i+1]
                i_lst.append(i)
        # remove zero and extra bits
        for i in i_lst[-1:-1-len(i_lst):-1]:
            t.pop(i+1)
            t.pop(i)
    print(len(t))
    print(*t)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        whatsNext(arr)
