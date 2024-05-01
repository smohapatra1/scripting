# #   https://www.hackerrank.com/challenges/similar-strings/problem?isFullScreen=true

# Jimmy loves playing with strings. He thinks string  is similar to string  if the following conditions are satisfied:

# Both strings have the same length (i.e.,  and ).
# For each valid pair of indices, , in the strings,  and  or  and .
# For example, string  and  are similar as for ,  and  and for all other  pairs  as well as .

# He has a string, , of size  and gives you  queries to answer where each query is in the form of a pair of integers . For each substring , find the number of substrings  where substring  is similar to substring  and print this number on a new line.

# Note: Substring  is the contiguous sequence of characters from index  to index . For example, if  abcdefgh, then  cdef.

# Input Format

# The first line contains two space-separated integers describing the respective values of  and .
# The second line contains string .
# Each line  of the  subsequent lines contains two space-separated integers describing the respective values of  and  for query .

# Constraints

# Output Format

# For each query, print the number of similar substrings on a new line.

# Sample Input

# 8 4
# giggabaj
# 1 1
# 1 2
# 1 3
# 2 4
# Sample Output

# 8
# 6
# 2
# 1
# Explanation

# We perform the following sequence of queries:

# Strings with length  are all similar, so our answer is .
# gi, ig, ga, ab, ba, and aj are similar, so our answer is .
# gig and aba are similar, so our answer is .
# igg has no similar string, so our answer is .



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'similarStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def extract_map2(subst):
    pairs_ = []
    len_ = len(subst)
    follow_map = 0
    for s in range(len_-1):
        if follow_map & 1 == 0:
            follow_map >>= 1
            s_pairs_ = 0b0
            index = 0
            for e in range(s + 1, len_):
                if subst[s] == subst[e]:
                    s_pairs_ += 1 << index
                index += 1
            follow_map |= s_pairs_
            pairs_.append([s, s_pairs_])
        else:
            follow_map >>= 1
    return pairs_
        
# def extract_map(subst):
#     len_ = len(subst)
#     pairs_ = [0 for i in range(len_ - 1)]
#     follow_map = 0
#     for s in range(len_-1):
#         if follow_map & 1 == 0:
#             follow_map >>= 1
#             s_pairs_ = 0b0
#             index = 0
#             for e in range(s + 1, len_):
#                 if subst[s] == subst[e]:
#                     s_pairs_ += 1 << index
#                     if e != len_:
#                         pairs_[e] = s
#                 index += 1
#             follow_map |= s_pairs_
#             pairs_[s] = s_pairs_
#         else:
#             follow_map >>= 1
#             pairs_[s] = pairs_[ pairs_[s] ]  >> s
#     return pairs_
    
def extract_map(subst):
    pairs_ = []
    len_ = len(subst)
    for s in range(len_-1):
        s_pairs_ = 0b0
        index = 0
        for e in range(s + 1, len_):
            if subst[s] == subst[e]:
                s_pairs_ += 1 << index
            index += 1
        pairs_.append(s_pairs_)
    return pairs_

def extract_submap(map_, s, e):
    pairs_ = []
    len_ = e - s - 1
    mask = 2 ** len_ - 1
    for s_ in range(s, e - 1):
        pairs_.append( map_[s_] &  mask )
        mask >>= 1
    return pairs_
    
def similarStrings(n, queries):
    # Write your code here
    out = []
    s_map = extract_map(n)
    s_len = len(n)
    for s, e in queries:
        ss_map = extract_submap(s_map, s - 1, e)
        ss_len = e - s + 1
        sss_len = s_len
        if ss_len > 1:
            candidates = list(range(s_len - ss_len + 1))
            len_ = ss_len - 1
            mask = 2 ** len_ - 1
            for s_ in ss_map:
                candidates = [
                    st + 1 \
                    for st in candidates \
                    if s_map[st] & mask == s_ 
                ]
                mask >>= 1
            sss_len = len(candidates)
        out.append(sss_len)
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []
    
    n = str(input().strip())
    
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = similarStrings(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
