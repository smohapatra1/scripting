# #   https://www.hackerrank.com/challenges/tutzki-and-lcs/problem?isFullScreen=true

# Given two strings,  and , find and print the total number of ways to insert a character at any position in string  such that the length of the Longest Common Subsequence of characters in the two strings increases by one.

# Input Format

# The first line contains a single string denoting .
# The second line contains a single string denoting .

# Constraints

# Scoring

# Strings  and  are alphanumeric (i.e., consisting of arabic digits and/or upper and lower case English letters).
# The new character being inserted must also be alphanumeric (i.e., a digit or upper/lower case English letter).
# Subtask

#  for  of the maximum score.
# Output Format

# Print a single integer denoting the total number of ways to insert a character into string  in such a way that the length of the longest common subsequence of  and  increases by one.

# Sample Input

# aa
# baaa
# Sample Output

# 4
# Explanation

# The longest common subsequence shared by  and  is aa, which has a length of . There are two ways that the length of the longest common subsequence can be increased to  by adding a single character to :

# There are  different positions in string  where we could insert an additional a to create longest common subsequence aaa (i.e., at the beginning, middle, and end of the string).
# We can insert a b at the beginning of the string for a new longest common subsequence of baa.
# As we have  ways to insert an alphanumeric character into  and increase the length of the longest common subsequence by one, we print  on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'tutzkiAndLcs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def tutzkiAndLcs(a, b):
    # Write your code here
    s1 = a
    s2 = b
    l1, l2 = len(s1), len(s2)
    d1 = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    d2 = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    cc = [0] * 256
    ret = 0
    
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            d1[i][j] = max(d1[i - 1][j], d1[i][j - 1])
            if s1[i - 1] == s2[j - 1]:
                d1[i][j] = d1[i - 1][j - 1] + 1
                
    for i in range(l1 - 1, -1, -1):
        for j in range(l2 - 1, -1, -1):
            d2[i][j] = max(d2[i + 1][j], d2[i][j + 1])
            if s1[i] == s2[j]:
                d2[i][j] = d2[i + 1][j + 1] + 1
                
    for i in range(l1 + 1):
        for j in range(l2):
            if d1[i][j] + d2[i][j + 1] == d1[l1][l2]:
                cc[ord(s2[j])] = 1
        ret += sum(cc)
        cc = [0] * 256
    
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = tutzkiAndLcs(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
