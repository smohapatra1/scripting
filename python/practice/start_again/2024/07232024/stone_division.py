# #   https://www.hackerrank.com/challenges/stone-division/problem?isFullScreen=true

# Consider the following game:

# There are two players, First and Second, sitting in front of a pile of  stones. First always plays first.
# There is a set, , of  distinct integers defined as .
# The players move in alternating turns. During each turn, a player chooses some  and splits one of the piles into exactly  smaller piles of equal size. If no  exists that will split one of the available piles into exactly  equal smaller piles, the player loses.
# Both players always play optimally.
# Given , , and the contents of , find and print the winner of the game. If First wins, print First; otherwise, print Second.

# Input Format

# The first line contains two space-separated integers describing the respective values of  (the size of the initial pile) and  (the size of the set).
# The second line contains  distinct space-separated integers describing the respective values of .

# Constraints

# Output Format

# Print First if the First player wins the game; otherwise, print Second.

# Sample Input 0

# 15 3
# 5 2 3
# Sample Output 0

# Second
# Explanation 0

# The initial pile has  stones, and . During First's initial turn, they have two options:

# Split the initial pile into  equal piles, which forces them to lose after the following sequence of turns:
# stone-division.png
# Split the initial pile into  equal piles, which forces them to lose after the following sequence of turns:
# stone-division-2.png
# Because First never has any possible move that puts them on the path to winning, we print Second as our answer.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stoneDivision' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER_ARRAY s
#


def solve(n) :
    if n in D :
        return D[n]
    for k in S :
        if n%k == 0 :
            x = n//k
            if solve(x) :
                if k%2 == 0 :
                    D[n] = True
                    return True
            else :
                D[n] = True
                return True
    D[n] = False
    return False

n, m = [int(i) for i in input().split()]
S = [int(i) for i in input().split()]
D = {1:False}
print("First" if solve(n) else "Second")

# def stoneDivision(n, s):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     s = list(map(int, input().rstrip().split()))

#     result = stoneDivision(n, s)

#     fptr.write(result + '\n')

#     fptr.close()
