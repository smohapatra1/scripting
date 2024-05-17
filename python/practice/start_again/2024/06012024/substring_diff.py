# #   https://www.hackerrank.com/challenges/substring-diff/problem?isFullScreen=true

# In this problem, we'll use the term "longest common substring" loosely. It refers to substrings differing at some number or fewer characters when compared index by index. For example, 'abc' and 'adc' differ in one position, 'aab' and 'aba' differ in two.

# Given two strings and an integer , determine the length of the longest common substrings of the two strings that differ in no more than  positions.

# For example, . Strings  and . Check to see if the whole string (the longest substrings) matches. Given that neither the first nor last characters match and , we need to try shorter substrings. The next longest substrings are  and . Two pairs of these substrings only differ in  position:  and . They are of length .

# Function Description

# Complete the substringDiff function in the editor below. It should return an integer that represents the length of the longest common substring as defined.

# substringDiff has the following parameter(s):

# k: an integer that represents the maximum number of differing characters in a matching pair
# s1: the first string
# s2: the second string
# Input Format

# The first line of input contains a single integer, , the number of test cases follow.
# Each of the next  lines contains three space-separated values: an integer  and two strings,  and .

# Constraints

# All characters in  and .
# Output Format

# For each test case, output a single integer which is the length of the maximum length common substrings differing at  or fewer positions.

# Sample Input

# 3
# 2 tabriz torino
# 0 abacba abcaba
# 3 helloworld yellomarin
# Sample Output

# 4
# 3
# 8
# Explanation

# First test case: If we take "briz" from the first string, and "orin" from the second string, then the number of mismatches between these two substrings is equal to 2 and their lengths are .

# Second test case: Since , we should find the longest common substring, standard definition, for the given input strings. We choose "aba" as the result.

# Third test case: We can choose "hellowor" from first string and "yellomar" from the second string.



#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'substringDiff' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s1
#  3. STRING s2
#

def substringDiff(k, s1, s2):
    # Write your code here
    def matches(str1, str2):
        maxLen = 0
        lengthS1 = len(str1)
        lengthS2 = len(str1)
        for idx in range(lengthS1):
            j = 0
            queue = deque()
            res = [0] * 2
            trackLen = 0
            for i in range(idx, lengthS1):
                if j > lengthS2: # ensure doesnt exceed
                    break
                    
                if str1[i] == str2[j]:
                    res[1] += 1
                    queue.append(1)
                    trackLen += 1
                else: 
                    res[0] += 1
                    queue.append(0)
                    trackLen += 1
                while res[0] > k:
                    val = queue.popleft()
                    res[val] -= 1
                    trackLen -= 1
                if trackLen > maxLen:
                    maxLen = trackLen
                j += 1
        return maxLen

    return max(matches(s1, s2), matches(s2, s1))
                     
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        k = int(first_multiple_input[0])

        s1 = first_multiple_input[1]

        s2 = first_multiple_input[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
