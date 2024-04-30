# #   https://www.hackerrank.com/challenges/super-functional-strings/problem?isFullScreen=true

# We define a function, , on a string, , as follows:

# where:

#  denotes the number of characters in string .
#  denotes the number of distinct characters in string .
# Consuela loves creating string challenges and she needs your help testing her newest one! Given a string, , consisting of  lowercase letters, compute the summation of function  (provided above) over all possible distinct substrings of . As the result is quite large, print it modulo .

# Input Format

# The first line contains a single integer, , denoting the number of test cases.
# Each of the  subsequent lines contains a string, .

# Constraints

# The sum of  over all test cases does not exceed .
# Scoring

#  for  of test data.
#  for  of test data.
#  for  of test data.
# Output Format

# For each test case, print the answer modulo .

# Sample Input

# 3
# aa
# aba
# abc
# Sample Output

# 3
# 19
# 38
# Explanation

# Test 0:

#  and  are the only distinct substrings.


# Test 1:

# , , , , and  are the only distinct substrings.


#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase
from bisect import bisect_left, bisect_right
from itertools import zip_longest, islice

#
# Complete the 'superFunctionalStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


MOD = 7 + 10 ** 9

N = 10 ** 5

sum_pow = [[0] * (N + 1) for k in range(27)]
for k in range(1, 27):
    for n in range(1, N + 1):
        sum_pow[k][n] = (sum_pow[k][n - 1] + pow(n, k, MOD)) % MOD
        
        
def get_sp(left, right, k):
    if left > right or right <= 0:
        return 0
    if left <= 0:
        return sum_pow[k][right]
    return (sum_pow[k][right] + MOD - sum_pow[k][left - 1]) % MOD


def all_occ(s):
    n = len(s)
    occ = [[] for _ in range(26)]
    for i in range(n):
        occ[ord(s[i]) - ord('a')].append(i)
    return occ

def occ_from_i(occ, i):
    occ_i = []
    for j in range(26):
        if len(occ[j]) == 0 or i > occ[j][-1]:
            continue
        first = bisect_left(occ[j], i)
        occ_i.append(occ[j][first])
    return sorted(occ_i)


def sorted_idx(items):
    unique = sorted(set(items))
    idx = dict(zip(unique, range(len(unique))))
    return [idx[v] for v in items]

def suffix_array(s):
    n = len(s)
    k = 1
    sa = sorted_idx(s)
    while max(sa) < n - 1:
        sa = sorted_idx([a * (n + 1) + b + 1 for
                         (a, b) in zip_longest(sa,
                                               islice(sa, k, None),
                                               fillvalue=-1)])
        k <<= 1
    return sa

def lcp_sa(s):
    inv_sa = suffix_array(s)
    n = len(inv_sa)
    sa = [0] * n
    for i in range(n):
        sa[inv_sa[i]] = i
    lcp = [0] * n
    k = 0
    for i in range(n):
        if inv_sa[i] == n - 1:
            k = 0
            continue
        j = sa[inv_sa[i]+1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[inv_sa[i] + 1] = k
        if k > 0:
            k -= 1
    return sa, lcp

def solve(s):
    n = len(s)
    occ = all_occ(s)
    sa, lcp = lcp_sa(s)
    ans = 0
    #print(sa)
    #print(lcp)
    for i in range(n):
        o = occ_from_i(occ, sa[i])
        t = sa[i] + lcp[i]
        if t >= o[-1]:
            ans = (ans + get_sp(lcp[i] + 1, n - sa[i], len(o))) % MOD
            continue
        k = bisect_right(o, t)
        ans = (ans + get_sp(lcp[i] + 1, o[k] - sa[i], k)) % MOD
        for j in range(k + 1, len(o)):
            ans = (ans + get_sp(o[j - 1] - sa[i] + 1, o[j] - sa[i], j)) % MOD
        
        ans = (ans + get_sp(o[-1] - sa[i] + 1, n - sa[i], len(o))) % MOD
        
    return ans

def sum_p_bf(left, right, k):
    ans = 0
    for n in range(max(left, 1), right + 1):
        ans = (ans + pow(n, k, MOD)) % MOD
    return ans

q = int(input().strip())
for _ in range(q):
    string = input().strip()
    print(solve(string))

