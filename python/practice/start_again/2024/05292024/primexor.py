# #   https://www.hackerrank.com/challenges/prime-xor/problem?isFullScreen=true

# Penny has an array of  integers, . She wants to find the number of unique multisets she can form using elements from the array such that the bitwise XOR of all the elements of the multiset is a prime number. Recall that a multiset is a set which can contain duplicate elements.

# Given  queries where each query consists of an array of integers, can you help Penny find and print the number of valid multisets for each array? As these values can be quite large, modulo each answer by  before printing it on a new line.

# Input Format

# The first line contains a single integer, , denoting the number of queries. The  subsequent lines describe each query in the following format:

# The first line contains a single integer, , denoting the number of integers in the array.
# The second line contains  space-separated integers describing the respective values of .
# Constraints

# Output Format

# On a new line for each query, print a single integer denoting the number of unique multisets Penny can construct using numbers from the array such that the bitwise XOR of all the multiset's elements is prime. As this value is quite large, your answer must be modulo .

# Sample Input

# 1   
# 3   
# 3511 3671 4153  
# Sample Output

# 4
# Explanation

# The valid multisets are:

#  is prime.
#  is prime.
#  is prime.
# , which is prime.
# Because there are four valid multisets, we print the value of  on a new line.


#!/bin/python3

from math import sqrt
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'primeXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# Complete the primeXor function below.
def middle_out(counts):
    a = ((4096, 4351), (4352, 4500), (3584, 4095), (3500, 3583))
    b = ((256, 0), (512, 0), (512, 4096), (1024, 4096))
    divisor = 0
    count = [0]*4501
    for i,n in counts:
        count[i] = n

    sum = [[0]*8192 for _ in range(2)] 
    temp, update = 0, 1 
    sum[temp][0] = 1 
    divisor = 10**9 + 7
    for i,p in enumerate(a):
        for j,n in enumerate(count[p[0]:p[1]+1]):
            if n:
                temp2 = n//2 
                same = 1 + temp2
                change = (n+1)//2  
                o = b[i][1]
                for x in range(b[i][0]):  
                    y = x^(j+p[0])
                    sum[update][y] = (sum[temp][x]*change + sum[temp][y]*same)
                    sum[update][x] = (sum[temp][y]*change + sum[temp][x]*same)
                    
                    if o:
                        sum[update][y+o] = (sum[temp][x+o]*change + sum[temp][y+o]*same)
                        sum[update][x+o] = (sum[temp][y+o]*change + sum[temp][x+o]*same)
                        
                if sum[update][0] > 100000*divisor:  
                    for x in range(len(sum[update])):
                        sum[update][x] %= divisor
                temp, update = update, temp

    p = primes(8191)
    total = 0
    for prime in p:
        total += sum[temp][prime]
    return total % divisor

def primes(n):
    x = [True]*((n-1)//2)
    for i in range(int((sqrt(n)-3)//2)+1):
        if x[i]:
            x[2*i*i+6*i+3::2*i+3] = [False] * int((n-(2*i+3)**2)//(4*i+6)+1)
    return [2] + [2*i+3 for i,v in enumerate(x) if v]
q = int(input())
for _ in range(q):
    n = int(input())
    numbers = Counter(int(x) for x in input().split()).items()
    print(middle_out(numbers))
    


# def primeXor(a):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         a = list(map(int, input().rstrip().split()))

#         result = primeXor(a)

#         fptr.write(str(result) + '\n')

#     fptr.close()
