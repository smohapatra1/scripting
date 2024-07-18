# #   https://www.hackerrank.com/challenges/permutation-game/problem?isFullScreen=true

# Alice and Bob play the following game:

# They choose a permutation of the numbers  to .
# Alice plays first and they alternate.
# In a turn, they can remove any one remaining number from the permutation.
# The game ends when the remaining numbers form an increasing sequence of  or more numbers. The person who played the turn that leaves an increasing sequence wins the game.
# Assuming both play optimally, who wins the game? Return Alice or Bob.

# Example 

# This is the starting permutation to analyze, . First, Alice chooses  or . For the example, Alice chooses  and leaves . Since this is a decreasing sequence, Bob can remove any number for optimum play. He will lose regardless. Alice then removes any number leaving an array of only one element. Since Alice removed the last element to create an increasing sequence, Alice wins.

# Function Description

# Complete the permutationGame function in the editor below.

# permutationGame has the following parameter:
# - int arr[n]: the starting permutation

# Returns

# string: either Alice or Bob
# Input Format

# The first line contains the number of test cases .

# Each of the next  pairs of lines is in the following format:
# - The first line contains an integer , the size of the array 
# - The second line contains  space-separated integers,  where 

# Constraints

# The permutation will not be an increasing sequence initially.
# Sample Input

# STDIN       Function
# -----       --------
# 2           t = 2
# 3           arr[] size n = 3
# 1 3 2       arr = [1, 3, 2]
# 5           n = 5
# 5 3 2 1 4   arr = [5, 3, 2, 1, 4]
# Sample Output

# Alice
# Bob
# Explanation

# For the first test, Alice can remove  or  to leave an increasing sequence and win the game.

# For the second test, if  is removed then the only way to have an increasing sequence is to only have  number left. This takes a total of  moves, and Bob wins.

# If Alice removes the  on the first move, it will take  more moves to create an increasing sequence. Bob wins. If Alice removes something else, Bob can remove  on his next turn to create the same game state. It is a decreasing sequence with  numbers left.


#!/bin/python3

import math
import os
import random
import re
import sys
from functools import cache

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def permutationGame(arr):
    # Write your code here
    def is_increasing(remain):
        return all(remain[i] < remain[i+1] for i in range(len(remain)-1))
    def new_perm(remain, removed):
        return tuple(e - 1 if e > removed else e for e in remain if e != removed)
    @cache
    def first_wins(remain):
        if is_increasing(remain):
            return False
        return any(not first_wins(new_perm(remain, e)) for e in remain)
    return 'Alice' if first_wins(tuple(arr)) else 'Bob'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
