# #   https://www.hackerrank.com/challenges/accessory-collection/problem?isFullScreen=true

# Victoria is splurging on expensive accessories at her favorite stores. Each store stocks  types of accessories, where the  accessory costs  dollars (). Assume that an item's type identifier is the same as its cost, and the store has an unlimited supply of each accessory.

# Victoria wants to purchase a total of  accessories according to the following rule:

# Any -element subset of the purchased items must contain at least  different types of accessories.

# For example, if , , and , then she must choose  accessories such that any subset of  of the  accessories will contain at least  distinct types of items.

# Given , , , and  values for  shopping trips, find and print the maximum amount of money that Victoria can spend during each trip; if it's not possible for Victoria to make a purchase during a certain trip, print SAD instead. You must print your answer for each trip on a new line.

# Input Format

# The first line contains an integer, , denoting the number of shopping trips.
# Each of the  subsequent lines describes a single shopping trip as four space-separated integers corresponding to , , , and , respectively.

# Constraints

# The sum of the 's for all  shopping trips .
# Output Format

# For each shopping trip, print a single line containing either the maximum amount of money Victoria can spend; if there is no collection of items satisfying her shopping rule for the trip's , , , and  values, print SAD instead.

# Sample Input

# 2
# 6 5 3 2
# 2 1 2 2
# Sample Output

# 24
# SAD
# Explanation

# Shopping Trip 1:
# We know that:

# Victoria wants to buy  accessories.
# The store stocks the following  types of accessories: .
# For any grouping of  of her  accessories, there must be at least  distinct types of accessories.
# Victoria can satisfy her shopping rule and spend the maximum amount of money by purchasing the following set of accessories: . The total cost is , so we print  on a new line.

# Shopping Trip 2:
# We know that:

# Victoria wants to buy  accessories.
# The store stocks  type of accessory: .
# For any grouping of  of her  accessories, there must be at least  distinct types of accessories.
# Because the store only carries  type of accessory, Victoria cannot make a purchase satisfying the constraint that there be at least  distinct types of accessories. Because Victoria will not purchase anything, we print that she is SAD on a new line.


#!/bin/python3

import os
import sys

#
# Complete the acessoryCollection function below.
#
def acessoryCollection(L, A, N, D):
    #
    # Write your code here.
    #
    if D > A or N < D or N > L :
        return 'SAD'
    elif D == 1:
        return str(L * A) 
    else:
        res = 0 
        max = (N - 1) //(D - 1)
        for i in range(max, 0, -1):
            a1 = N + (i-1) - i * (D-1)
            n = (L - a1 )//i
            a3 = (L - a1) % i
            if n > A - 1 or n == A-1 and a3 > 0:
                break
            sum = A * a1 + (A-1 + A - n) * n //2 * i + a3 *(A -n-1)
            if sum <= res:
                break
            res = sum
        if res :
            return str(res)
        else:
            return 'SAD'
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        LAND = input().split()

        L = int(LAND[0])

        A = int(LAND[1])

        N = int(LAND[2])

        D = int(LAND[3])

        result = acessoryCollection(L, A, N, D)

        fptr.write(result + '\n')

    fptr.close()
