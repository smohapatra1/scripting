# #   https://www.hackerrank.com/challenges/hr-city/problem?isFullScreen=true


# HackerRank-city is an acyclic connected graph (or tree). Its not an ordinary place, the construction of the whole tree takes place in  steps. The process is described below:

# It initially has  node.
# At each step, you must create  duplicates of the current tree, and create  new nodes to connect all  copies in the following H shape:
# nik2.png

# At each  step, the tree becomes  times bigger plus  new nodes, as well as  new edges connecting everything together. The length of the new edges being added at step  is denoted by input .

# Calculate the sum of distances between each pair of nodes; as these answers may run large, print your answer modulo .

# Input Format

# The first line contains an integer,  (the number of steps). The second line contains  space-separated integers describing , .

# Constraints



# Subtask
# For  score 

# Output Format

# Print the sum of distances between each pair of nodes modulo .

# Sample Input 0

# 1
# 1
# Sample Output 0

# 29
# Sample Input 1

# 2
# 2 1
# Sample Output 1

# 2641
# Explanation

# Sample 0
# In this example, our tree looks like this:

# nik4.png

# Let  denote the distance between nodes  and .

#    .

# We print the result of  as our answer.

# Sample 1

# In this example, our tree looks like this: nik city2.png

# We calculate and sum the distances between nodes in the same manner as Sample 0 above, and print the result of our , which is .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankCity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY A as parameter.
#

def nnew(n, mod):
    return (4*n+2)%mod
def jnew(j, A, mod):
    return (2*j+3*A)%mod
def xnew(x, A, n, j, mod):
    return (A+5*A*n+4*x+(3*n+2)*(j+A) )%mod
def sumnew(sm, A, n, x, mod):
    return ( 4*sm + (3*A*n+2*x)*4 + A + (2*n*(2*x+2*n*A) + 4*n*(2*x+3*n*A) ) )%mod
    

def hackerrankCity(A):
    # Write your code here
    mod = 10**9 + 7
    N = len(A)
    j0 = x0 = sum0 = j1 = x1 = sum1 = 0
    n0 = n1 = 1
    for i in range(N):
        Ai = A[i]
        j1 = jnew(j0, Ai, mod)
        x1 = xnew(x0, Ai, n0, j0, mod)
        n1 = nnew(n0, mod)
        sum1 = sumnew(sum0, Ai, n0, x0, mod)
        j0=j1
        sum0=sum1
        n0=n1
        x0=x1
    return sum0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    result = hackerrankCity(A)

    fptr.write(str(result) + '\n')

    fptr.close()
