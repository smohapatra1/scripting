# #   https://www.hackerrank.com/challenges/bear-and-steady-gene/problem?isFullScreen=true

# A gene is represented as a string of length  (where  is divisible by ), composed of the letters , , , and . It is considered to be steady if each of the four letters occurs exactly  times. For example,  and  are both steady genes.

# Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string . It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of  and replace it with any string of the same length.

# Modifying a large substring of bear genes can be dangerous. Given a string , can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

# Note: A substring of a string  is a subsequence made up of zero or more contiguous characters of .

# As an example, consider . The substring  just before or after  can be replaced with  or . One selection would create .

# Function Description

# Complete the  function in the editor below. It should return an integer that represents the length of the smallest substring to replace.

# steadyGene has the following parameter:

# gene: a string
# Input Format

# The first line contains an interger  divisible by , that denotes the length of a string .
# The second line contains a string  of length .

# Constraints

#  is divisible by 
# Subtask

#  in tests worth  points.
# Output Format

# Print the length of the minimum length substring that can be replaced to make  stable.

# Sample Input

# 8  
# GAAATAAA
# Sample Output

# 5
# Explanation

# One optimal solution is to replace  with  resulting in .
# The replaced substring has length .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Write your code here
    N = len(gene)
    ans = (0, N)
    transDic = {'C':0, 'G':1, 'T':2, 'A':3}
    decGen = list(map(lambda x: transDic[x],gene))
    cnt = [0]*4
    for i in range(4):
        cnt[i] =decGen.count(i)
    if max(cnt) == N/4:
        return 0
    j = 0 
    for idx, nl in enumerate(decGen):
        j = max(idx, j)
        if j >=N:
            break
        while max(cnt) > N/4 and j < N:
            j +=1
            cnt[decGen[j-1]] -=1
        x, y = ans
        if max(cnt) <=N/4:
            if abs(x-y) > abs(idx -j ):
                ans = (idx, j)
        cnt[nl] +=1
    i, j = ans
    return abs(i-j) 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
