# #   https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=true

# A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are  to  from  to  as shown below:

# image

# The weight of a string is the sum of the weights of its characters. For example:

# image

# A uniform string consists of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not.
# Given a string, , let  be the set of weights for all possible uniform contiguous substrings of string . There will be  queries to answer where each query consists of a single integer. Create a return array where for each query, the value is Yes if . Otherwise, append No.

# Note: The  symbol denotes that  is an element of set .

# Example

# .

# Working from left to right, weights that exist are:

# string  weight
# a       1
# b       2
# bb      4
# c       3
# cc      6
# ccc     9
# d       4
# dd      8
# ddd     12
# dddd    16
# Now for each value in , see if it exists in the possible string weights. The return array is ['Yes', 'No', 'No', 'Yes', 'No'].

# Function Description

# Complete the weightedUniformStrings function in the editor below.

# weightedUniformStrings has the following parameter(s):
# - string s: a string
# - int queries[n]: an array of integers

# Returns
# - string[n]: an array of strings that answer the queries

# Input Format

# The first line contains a string , the original string.
# The second line contains an integer , the number of queries.
# Each of the next  lines contains an integer , the weight of a uniform subtring of  that may or may not exist.

# Constraints

#  will only contain lowercase English letters, ascii[a-z].
# Sample Input 0

# abccddde
# 6
# 1
# 3
# 12
# 5
# 9
# 10
# Sample Output 0

# Yes
# Yes
# Yes
# Yes
# No
# No
# Explanation 0

# The weights of every possible uniform substring in the string abccddde are shown below:

# image

# We print Yes on the first four lines because the first four queries match weights of uniform substrings of . We print No for the last two queries because there are no uniform substrings in  that have those weights.

# Note that while de is a substring of  that would have a weight of , it is not a uniform substring.

# Note that we are only dealing with contiguous substrings. So ccc is not a substring of the string ccxxc.

# Sample Input 1

# aaabbbbcccddd
# 5
# 9
# 7
# 8
# 12
# 5
# Sample Output 1

# Yes
# No
# Yes
# Yes
# No

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    d = {c:ord(c)-96 for c in set(s)}
    
    for i in range(len(queries)):
        res = "No"
        for c, w in d.items():
            if queries[i]%w==0 and c*(queries[i]//w) in s:
                res = "Yes"
                break
        queries[i] = res
    
    return queries
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
