# #   https://www.hackerrank.com/challenges/pmix/problem?isFullScreen=true

# Some scientists are working on protein recombination, and during their research, they have found a remarkable fact: there are 4 proteins in the protein ring that mutate after every second according to a fixed pattern. For simplicity, proteins are called  (you know, protein names can be very complicated). A protein mutates into another one depending on itself and the protein right after it. Scientists determined that the mutation table goes like this:

#     A   B   C   D
#     _   _   _   _
# A|  A   B   C   D
# B|  B   A   D   C
# C|  C   D   A   B
# D|  D   C   B   A
# Here rows denote the protein at current position, while columns denote the protein at the next position. And the corresponding value in the table denotes the new protein that will emerge. So for example, if protein i is A, and protein i + 1 is B, protein i will change to B. All mutations take place simultaneously. The protein ring is seen as a circular list, so last protein of the list mutates depending on the first protein.

# Using this data, they have written a small simulation software to get mutations second by second. The problem is that the protein rings can be very long (up to 1 million proteins in a single ring) and they want to know the state of the ring after upto  seconds. Thus their software takes too long to report the results. They ask you for your help.

# Input Format

# Input contains 2 lines.
# First line has 2 integers  and ,  being the length of the protein ring and  the desired number of seconds.
# Second line contains a string of length  containing uppercase letters ,,  or  only, describing the ring.

# Constraints



# Output Format

# Output a single line with a string of length , describing the state of the ring after  seconds.

# Sample Input 0

# 5 15
# AAAAD
# Sample Output 0

# DDDDA
# Explanation 0

# The complete sequence of mutations is:

# AAADD
# AADAD
# ADDDD
# DAAAD
# DAADA
# DADDD
# DDAAA
# ADAAD
# DDADD
# ADDAA
# DADAA
# DDDAD
# AADDA
# ADADA
# DDDDA

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pmix' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def pmix(s, k):
    # Write your code here
    c2i = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    i2c = ['A', 'B', 'C', 'D']
    l = [c2i[x] for x in s]
    l = [l, [0] * n]
    p=[0] * n

    a, b = 1, 0

    while k > 0:
        a ^= b
        b ^= a
        a ^= b
    
        cp2 = 1
        for i in range(29, 0, -1):
            if k - (1 << i) >= 0:
                cp2 = 1 << i
                break
                  
        k -= cp2
    
    
        for i in range(n):
            l[b][i] = l[a][i] ^ l[a][(i + cp2) % n]
        

    for i, j in zip(l[b], range(n)):
        p[j]=i2c[i]

                        
    r=''.join(p) 
    return r 

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = pmix(s, k)

    fptr.write(result + '\n')

    fptr.close()
