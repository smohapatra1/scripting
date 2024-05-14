# #   https://www.hackerrank.com/challenges/abbr/problem?isFullScreen=true

# You can perform the following operations on the string, :

# Capitalize zero or more of 's lowercase letters.
# Delete all of the remaining lowercase letters in .
# Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.

# For example, given  and , in  we can convert  and delete  to match . If  and , matching is not possible because letters may only be capitalized or discarded, not changed.

# Function Description

# Complete the function  in the editor below. It must return either  or .

# abbreviation has the following parameter(s):

# a: the string to modify
# b: the string to match
# Input Format

# The first line contains a single integer , the number of queries.

# Each of the next  pairs of lines is as follows:
# - The first line of each query contains a single string, .
# - The second line of each query contains a single string, .

# Constraints

# String  consists only of uppercase and lowercase English letters, ascii[A-Za-z].
# String  consists only of uppercase English letters, ascii[A-Z].
# Output Format

# For each query, print YES on a new line if it's possible to make string  equal to string . Otherwise, print NO.

# Sample Input

# 1
# daBcd
# ABC
# Sample Output

# YES
# Explanation

# image

# We have  daBcd and  ABC. We perform the following operation:

# Capitalize the letters a and c in  so that  dABCd.
# Delete all the remaining lowercase letters in  so that  ABC.
# Because we were able to successfully convert  to , we print YES on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
    res = {""}
    for let in a:
        new_res = {""}
        for c in res:
            trail_c = c+ let.upper()
            if b.startswith(trail_c):
                new_res.add(trail_c)
                if let.islower():
                    new_res.add(c)
            elif let.islower():
                new_res.add(c)
            else:
                continue
        res = new_res
    if b in res:
        return 'YES'
    else:
        return 'NO' 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
