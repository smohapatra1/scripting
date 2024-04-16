# #   https://www.hackerrank.com/challenges/xor-subsequence/problem?isFullScreen=true

# Consider an array, , of  integers (). We take all consecutive subsequences of integers from the array that satisfy the following:

# For example, if  our subsequences will be:

# For each subsequence, we apply the bitwise XOR () operation on all the integers and record the resultant value. Since there are  subsequences, this will result in  numbers.

# Given array , find the XOR sum of every subsequence of  and determine the frequency at which each number occurs. Then print the number and its respective frequency as two space-separated values on a single line.

# Input Format

# The first line contains an integer, , denoting the size of the array.
# Each line  of the  subsequent lines contains a single integer describing element .

# Constraints

# Output Format

# Print  space-separated integers on a single line. The first integer should be the number having the highest frequency, and the second integer should be the number's frequency (i.e., the number of times it appeared). If there are multiple numbers having maximal frequency, choose the smallest one.

# Sample Input 0

# 4
# 2
# 1
# 1
# 3
# Sample Output 0

# 1 3
# Explanation 0

# Let's find the XOR sum for all consecutive subsequences. We'll refer to the frequency of some number  as , and keep a running sum for each frequency:

# , frequencies: 
# , frequencies:  and 
# , frequencies:  and 
# , frequencies: , , and 
# , frequencies: , , and 
# , frequencies: , , , and 
# , frequencies: , , , and 
# , frequencies: , , , and 
# , frequencies: , , , and 
# , frequencies: , , , and 
# Our maximal frequency is , and the integers , , and  all have this frequency. Because more than one integer has this frequency, we choose the smallest one, which is . We then print the respective smallest number having the maximal frequency and the maximal frequency as a single line of space-separated values.


#!/bin/python3

import math
import os
import random
import re
import sys
from operator import xor
from itertools import accumulate
from collections import Counter

#
# Complete the 'xorSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#
POW2 = 2**16

#
# Complete the xorSubsequence function below.
#
xorSubsequence = lambda a: main(a)

# from wikipedia
def fwht(a) -> None:
    
    h = 1
    while h < len(a):
        for i in range(0, len(a), h * 2):
            for j in range(i, i + h):
                x = a[j]
                y = a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2

def main(seq):
    
    histogram = Counter(accumulate([0]+seq,xor))
    histogram = [histogram[value] for value in range(POW2)]
    
    fwht(histogram)
    histogram = [x*x for x in histogram]
    fwht(histogram)
    histogram = [y//POW2 for y in histogram]
    
    histogram[0] -= len(seq)+1 # self combos (diagonal in table)
    histogram =[y//2 for y in histogram] # don't count things twice
    max_freq = max(histogram)
    return next((i,freq) for i,freq in enumerate(histogram) if freq ==max_freq)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = xorSubsequence(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
