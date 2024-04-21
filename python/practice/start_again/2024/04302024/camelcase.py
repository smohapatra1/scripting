# #   https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

# There is a sequence of words in CamelCase as a string of letters, , having the following properties:

# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given , determine the number of words in .

# Example

# There are  words in the string: 'one', 'Two', 'Three'.

# Function Description

# Complete the camelcase function in the editor below.

# camelcase has the following parameter(s):

# string s: the string to analyze
# Returns

# int: the number of words in 
# Input Format

# A single line containing string .

# Constraints

# Sample Input

# saveChangesInTheEditor
# Sample Output

# 5
# Explanation

# String  contains five words:

# save
# Changes
# In
# The
# Editor
# Need help? Try this problem first to get familiar with HackerRank environment.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    # return (len([i for i in s if i.isupper() ])) +1
    return len(re.split(r'[A-Z]', s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
