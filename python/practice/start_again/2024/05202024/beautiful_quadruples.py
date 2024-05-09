# #   https://www.hackerrank.com/challenges/xor-quadruples/problem?isFullScreen=true

# We call an quadruple of positive integers, , beautiful if the following condition is true:

# Note:  is the bitwise XOR operator.

# Given , , , and , count the number of beautiful quadruples of the form  where the following constraints hold:

# When you count the number of beautiful quadruples, you should consider two quadruples as same if the following are true:

# They contain same integers.
# Number of times each integers occur in the quadruple is same.
# For example  and  should be considered as same.

# Input Format

# A single line with four space-separated integers describing the respective values of , , , and .

# Constraints

# For  of the maximum score, 
# Output Format

# Print the number of beautiful quadruples.

# Sample Input

# 1 2 3 4
# Sample Output

# 11
# Explanation

# There are  beautiful quadruples for this input:

# Thus, we print  as our output.

# Note that  is same as .



#!/bin/python3

import os
import sys

#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
    #
    arr=[a,b,c,d]
    arr.sort()
    A=arr[0]
    B=arr[1]
    C=arr[2]
    D=arr[3]
    ans=0
    
    total=[0]*3001
    
    for i in range(1,A+1):
        for j in range(i,B+1):
            total[j]+=1
            
    for i in range(1,3001):
        total[i]+=total[i-1]
        
    count=[[0 for i in range(4097)] for j in range(3001)]
    
    print(count[0][0])
    
    for i in range(1,A+1):
        for j in range(i,B+1):
            e=i^j
            count[j][e]+=1
            
    print(count[0][0])
            
    for i in range(0,4097):
        for j in range(1,3001):
            count[j][i]+=count[j-1][i]
            
    
    for i in range(1,C+1):
        for j in range(i,D+1):
            ans+=(total[i]-count[i][i^j])
            
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()
