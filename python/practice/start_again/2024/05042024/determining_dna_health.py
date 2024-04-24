# #   https://www.hackerrank.com/challenges/determining-dna-health/problem?isFullScreen=true

# DNA is a nucleic acid present in the bodies of living things. Each piece of DNA contains a number of genes, some of which are beneficial and increase the DNA's total health. Each gene has a health value, and the total health of a DNA is the sum of the health values of all the beneficial genes that occur as a substring in the DNA. We represent genes and DNA as non-empty strings of lowercase English alphabetic letters, and the same gene may appear multiple times as a susbtring of a DNA.

# Given the following:

# An array of beneficial gene strings, . Note that these gene sequences are not guaranteed to be distinct.
# An array of gene health values, , where each  is the health value for gene .
# A set of  DNA strands where the definition of each strand has three components, , , and , where string  is a DNA for which genes  are healthy.
# Find and print the respective total healths of the unhealthiest (minimum total health) and healthiest (maximum total health) strands of DNA as two space-separated values on a single line.

# Input Format

# The first line contains an integer, , denoting the total number of genes.
# The second line contains  space-separated strings describing the respective values of  (i.e., the elements of ).
# The third line contains  space-separated integers describing the respective values of  (i.e., the elements of ).
# The fourth line contains an integer, , denoting the number of strands of DNA to process.
# Each of the  subsequent lines describes a DNA strand in the form start end d, denoting that the healthy genes for DNA strand  are  and their respective correlated health values are .

# Constraints

#  the sum of the lengths of all genes and DNA strands 
# It is guaranteed that each  consists of lowercase English alphabetic letters only (i.e., a to z).
# Output Format

# Print two space-separated integers describing the respective total health of the unhealthiest and the healthiest strands of DNA.

# Sample Input 0

# 6
# a b c aa d b
# 1 2 3 4 5 6
# 3
# 1 5 caaab
# 0 4 xyz
# 2 4 bcdybc
# Sample Output 0

# 0 19
# Explanation 0

# In the diagrams below, the ranges of beneficial genes for a specific DNA on the left are highlighed in green and individual instances of beneficial genes on the right are bolded. The total healths of the  strands are:

# image
# The total health of caaab is .
# image
# The total health of xyz is , because it contains no beneficial genes.
# image
# The total health of bcdybc is .
# The unhealthiest DNA strand is xyz with a total health of , and the healthiest DNA strand is caaab with a total health of . Thus, we print 0 19 as our answer.


#!/bin/python3

import math
import os
import random
import re
import sys
from math import inf
from collections import defaultdict
from bisect import bisect_left, bisect_right

def getHealth(seq, first, last, longest):
    h, ls = 0, len(seq)
    for l in range(ls):
        for k in range(1, longest+1):
            if l+k > ls:
                break
            sub = seq[l:l+k]
            if sub not in sub_d: 
            # if AA not in subs, AAA also not in subs
                break
            if sub not in gDict: 
            # if AA not in subs, AAA can be in gDict
                continue
            idxs, hs = gDict[sub]
            
            right = hs[bisect_right(idxs, last)] # O(logN)
            left = hs[bisect_left(idxs, first)]  # O(logN)
            h += (right - left)
    return h

if __name__ == '__main__':
    n = int(input().strip())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    gDict = defaultdict(lambda : [[], [0]]) # gene_idx, health
    sub_d = set() # substring of d
    
    for i, gene in enumerate(genes):
        gDict[gene][0].append(i) 
        # append gene index
        for j in range(1, min(len(gene), 50)+1):
            sub_d.add(gene[:j]) 
            # add substrings to subs
            
    for v in gDict.values():
        for i, idx in enumerate(v[0]):
            v[1].append(v[1][i]+health[idx]) 
            # cumulative sum of health (first index = 0)
    
    longest = max(list(map(len, genes))) # longest length of genes
    hMin, hMax = inf, 0

    s = int(input().strip())

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        
        h = getHealth(d, first, last, longest)
        hMin, hMax = min(hMin,h), max(hMax,h)

    print(hMin, hMax)
