# #   https://www.hackerrank.com/challenges/changing-bits/problem?isFullScreen=true


# Let a and b be binary numbers of length n (MSB to the left). The following commands may be performed:

# set_a idx x: Set  to , where  and  is  least significant bit of .
# set_b idx x: Set  to , where  and  is  least significant bit of .
# get_c idx: Print , where  and .
# Given , and a list of commands, create a string made of the results of each  call, the only command that produces output. For example,  and  so the length of the numbers is . Print an answer string that contains the results of all commands on one line. A series of commands and their results follow:

# Starting
# ans = '' (empty string)
# a b
# 000 111
# set_a 1 1
# 010 111
# set_b 0 1
# 010 111
# get_c 3
# a + b = 1001
# ans = '1'
# 010 111
# get_c 4
# a + b = 01001
# ans = '10'

# Note: When the command is get_c 4,  had to be padded to the left with a  to be long enough to return a value.

# Function Description

# Complete the changeBits function in the editor below. For each get_c command, it should print either a 0 or a 1 without a newline until all commands have been processed. At that point, add a newline.

# changeBits has the following parameters:
# - a, b: two integers represented as binary strings
# - queries[queries[0]-queries[n-1]]: an array of query strings in the format described

# Input Format

# The first line of input contains two space-separated integers,  and , the length of the binary representations of  and , and the number of commands, respectively.
# The second and third lines each contain a string representation of  and .
# The following  lines each contain a command string  as described above.

# Constraints



# Output Format

# For each query of the type , output a single digit 0 or 1. Output must be placed on a single line.

# Sample Input 0

# 5 5
# 00000
# 11111
# set_a 0 1
# get_c 5
# get_c 1
# set_b 2 0
# get_c 5
# Sample Output 0

# 100
# Explanation 0

# set_a 0 1 sets 00000 to 00001
# C = A + B = 00001 + 11111 = 100000, so get_c[5] = 1
# from the above computation get_c[1] = 0
# set_b 2 0 sets 11111 to 11011
# C = A + B = 00001 + 11011 = 011100, so get_c[5] = 0
# The output is hence concatenation of 1, 0 and 0 = 100

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'changeBits' function below.
#
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING_ARRAY queries
#

def changeBits(a, b, queries):
    # Write your code here
    a = int(a,2)
    b = int(b,2)
    for q in queries:
        q = q.rstrip().split()
        i = int(q[1])
        if q[0] == 'set_a':
            if q[2] == '1':
                a |= 1<< i
            else:
                a &= ~(1<<i)
        elif q[0] == 'set_b':
            if q[2] == '1':
                b |=1<<i
            else:
                b &= ~(1<<i)
        else:
            c = a +b
            if not c & (1<<i):
                print ('0', end ="")
            else:
                print (1, end="")
                 

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    ab_size = int(first_multiple_input[0])

    queries_size = int(first_multiple_input[1])

    a = input()

    b = input()

    queries = []

    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)

    changeBits(a, b, queries)
