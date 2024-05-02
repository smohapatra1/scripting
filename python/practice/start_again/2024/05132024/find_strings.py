# #   https://www.hackerrank.com/challenges/find-strings/problem?isFullScreen=true

# A substring is defined as a contiguous sequence of one or more characters in the string. More information on substrings can be found here.

# You are given n strings w[1], w[2], ......, w[n]. Let S[i] denote the set of all distinct substrings of the string w[i]. Let , that is, S is a set of strings that is the union of all substrings in all sets S[1], S[2], ..... S[n]. There will be many queries. For each query you will be given an integer 'k'. Your task is to find the kth element of the -indexed lexicographically ordered set of substrings in the set S. If there is no element , return INVALID.

# For example, your strings are . All of the substrings are  and . Combine the two sets and sort them to get . So, for instance if , we return 'a'. If , we return 'bc'. If  though, there is not an  so we return INVALID.

# Function Description

# Complete the findStrings function in the editor below. It should return array of strings.

# findStrings has the following parameter(s):

# w: an array of strings
# queries: an array of integers
# Input Format

# The first line contains an integer n, the number of strings in the array .
# Each of the next n lines consists of a string .
# The next line contains an integer q, the number of queries.
# Each of the next q lines consists of a single integer k.

# Constraints





# Each character of 

# Output Format

# Return an array of q strings where the ith string is the answer to the ith query. If a  is invalid, return "INVALID" for that case.

# Sample Input

# 2
# aab
# aac
# 3
# 3
# 8
# 23

# Sample Output

# aab
# c
# INVALID

# Explanation

# For the sample test case, we have 2 strings "aab" and "aac".
# S1 = {"a", "aa", "aab", "ab", "b"} . These are the 5 unique substrings of "aab".
# S2 = {"a", "aa", "aac",  "ac", "c" } . These are the 5 unique substrings of "aac".
# Now, S = {S1 U S2} = {"a", "aa", "aab", "aac", "ab", "ac", "b", "c"}. Totally, 8 unique strings are present in the set S.
# The lexicographically 3rd smallest string in S is "aab" and the lexicographically 8th smallest string in S is "c". Since there are only 8 distinct substrings, the answer to the last query is "INVALID".


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY w
#  2. INTEGER_ARRAY queries
#
sys.setrecursionlimit(20000)

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __str__(self):
        return self.print('')

    def print(self, prefix):
        desc = prefix + self.val + ':\n'
        
        desc += ''.join(map(lambda c: c.print(prefix + '  '), self.children))
        
        return desc

    def addChildNode(self, childNode):
        self.children.append(childNode)
        self.children.sort(key=lambda n:n.val)

    def addString(self, string):
        for child in self.children:
            if string.startswith(child.val):
                child.addString(string[len(child.val):])
                return
            if child.val.startswith(string):
                return
            if child.val == string:
                return

        for child in self.children:
            prefix = getSharedPrefix(child.val, string)
            
            if len(prefix):
                newVal = string[len(prefix):]

                newChild = Node(child.val[len(prefix):])
                newChild.children = child.children.copy()

                if newVal < newChild.val:
                    child.children = [Node(newVal), newChild]
                else:
                    child.children = [newChild, Node(newVal)]

                child.val = prefix
                return
                
        self.addChildNode(Node(string))

    def getSubstring(self, i):
        if i <= len(self.val):
            return self.val[:i]

        i -= len(self.val)

        for child in self.children:
            numSubstrings = child.getNumSubstrings()
            if i <= numSubstrings:
                return self.val + child.getSubstring(i)
            i -= numSubstrings

    def getNumSubstrings(self):
        total = len(self.val)
        for child in self.children:
            total += child.getNumSubstrings()

        return total

    

def getSharedPrefix(a, b):
    maxLen = min(len(a), len(b))
    for i in range(maxLen):
        if a[i] != b[i]:
            return a[:i]

    return a[:maxLen]
    
def findStrings(w, queries):
    # Write your code here
    allStrings = Node('')
    
    result = []
    
    for input_string in w:
        addAllSubstrings(input_string, allStrings)
    
    numStrings = allStrings.getNumSubstrings()
    print(allStrings)
    print('size',numStrings)
    
    for query in queries:
        if query > numStrings:
            result.append('INVALID')
        else:
            result.append(allStrings.getSubstring(query))
    return result

def getSubstring(strings, i):
    for string in strings:
        if i < len(string):
            return string[:i + 1]
        i -= len(string)
        
def addAllSubstrings(string, strings):
    for i in range(len(string)):
        # print(strings)
        # print('adding ' + string[i:])
        strings.addString(string[i:])
        
def addString(string, strings):
    print(string)
    if string in strings:
        return
  
    for i in range(len(strings)):
        if strings[i].startswith(string):
            return
        elif string.startswith(strings[i]):
            strings[i] = string
            return
    
    strings.append(string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    w_count = int(input().strip())

    w = []

    for _ in range(w_count):
        w_item = input()
        w.append(w_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = findStrings(w, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
