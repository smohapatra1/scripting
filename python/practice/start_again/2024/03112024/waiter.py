# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-waiter/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three
# You are a waiter at a party. There is a pile of numbered plates. Create an empty  array. At each iteration, , remove each plate from the top of the stack in order. Determine if the number on the plate is evenly divisible by the  prime number. If it is, stack it in pile . Otherwise, stack it in stack . Store the values in  from top to bottom in . In the next iteration, do the same with the values in stack . Once the required number of iterations is complete, store the remaining values in  in , again from top to bottom. Return the  array.

# Example



# An abbreviated list of primes is . Stack the plates in reverse order.



# Begin iterations. On the first iteration, check if items are divisible by .


# Move  elements to .


# On the second iteration, test if  elements are divisible by .


# Move  elmements to .


# And on the third iteration, test if  elements are divisible by .


# Move  elmements to .


# All iterations are complete, so move the remaining elements in , from top to bottom, to .

# . Return this list.

# Function Description

# Complete the waiter function in the editor below.

# waiter has the following parameters:

# int number[n]: the numbers on the plates
# int q: the number of iterations
# Returns

# int[n]: the numbers on the plates after processing
# Input Format

# The first line contains two space separated integers,  and .
# The next line contains  space separated integers representing the initial pile of plates, i.e., .

# Constraints




# Sample Input

# 5 1
# 3 4 7 6 5
# Sample Output

# 4
# 6
# 3
# 7
# 5
# Explanation

# Initially:

#  = [3, 4, 7, 6, 5]<-TOP

# After 1 iteration:

#  = []<-TOP

#  = [6, 4]<-TOP

#  = [5, 7, 3]<-TOP

# We should output numbers in  first from top to bottom, and then output numbers in  from top to bottom.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def first_prime(n):
    primes=[]
    num=2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num +=1
    return primes
    

def waiter(number, q):
    # Write your code here
    primes=first_prime(q)
    answers=[]
    arr=number
    for p in primes:
        B=[]
        A=[]
        for e in arr:
            if e % p == 0:
                B.append(e)
            else:
                A.append(e)
        answers+=B
        arr=A[::-1]
    answers +=A
    return answers

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)
    print (result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
