# #   https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true


# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

# Example

# The list of all anagrammatic pairs is  at positions  respectively.

# Function Description

# Complete the function sherlockAndAnagrams in the editor below.

# sherlockAndAnagrams has the following parameter(s):

# string s: a string
# Returns

# int: the number of unordered anagrammatic pairs of substrings in 
# Input Format

# The first line contains an integer , the number of queries.
# Each of the next  lines contains a string  to analyze.

# Constraints



#  contains only lowercase letters in the range ascii[a-z].

# Sample Input 0

# 2
# abba
# abcd
# Sample Output 0

# 4
# 0
# Explanation 0

# The list of all anagrammatic pairs is  and  at positions  and  respectively.

# No anagrammatic pairs exist in the second query as no character repeats.

# Sample Input 1

# 2
# ifailuhkqq
# kkkk
# Sample Output 1

# 3
# 10
# Explanation 1

# For the first query, we have anagram pairs  and  at positions  and  respectively.

# For the second query:
# There are 6 anagrams of the form  at positions  and .
# There are 3 anagrams of the form  at positions  and .
# There is 1 anagram of the form  at position .

# Sample Input 2

# 1
# cdcd
# Sample Output 2

# 5
# Explanation 2

# There are two anagrammatic pairs of length :  and .
# There are three anagrammatic pairs of length :  at positions  respectively.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    check_list = ""
    curr_list = ""
    res = 0 
    for i in range(len(s)):
        for k in range(i, len(s)):
            curr_list +=(s[k])
            for j in range(i+1, len(s)):
                check_list +=s[j]
                if len(check_list) == len(curr_list):
                    if sorted(check_list) == sorted(curr_list):
                        res +=1
                    check_list = check_list[1:]
            check_list = ""
        curr_list = ""
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
