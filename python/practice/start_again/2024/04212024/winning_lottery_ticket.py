# #   https://www.hackerrank.com/challenges/winning-lottery-ticket/problem?isFullScreen=true

# The SuperBowl Lottery is about to commence, and there are several lottery tickets being sold, and each ticket is identified with a ticket ID. In one of the many winning scenarios in the Superbowl lottery, a winning pair of tickets is:

# Concatenation of the two ticket IDs in the pair, in any order, contains each digit from  to  at least once.
# For example, if there are  distinct tickets with ticket ID  and ,  is a winning pair.

# NOTE: The ticket IDs can be concantenated in any order. Digits in the ticket ID can occur in any order.

# Your task is to find the number of winning pairs of distinct tickets, such that concatenation of their ticket IDs (in any order) makes for a winning scenario. Complete the function winningLotteryTicket which takes a string array of ticket IDs as input, and return the number of winning pairs.

# Input Format

# The first line contains  denoting the total number of lottery tickets in the super bowl.
# Each of the next  lines contains a string, where string on a  line denotes the ticket id of the  ticket.

# Constraints

#  length of  
# sum of lengths of all 
# Each ticket id consists of digits from 
# Output Format

# Print the number of pairs in a new line.

# Sample Input 0

# 5
# 129300455 
# 5559948277
# 012334556 
# 56789
# 123456879
# Sample Output 0

# 5
# Explanation 0

# Pairs of distinct tickets that make for a winning scenario are :

# Ticket ID 1	Ticket ID 2	Winning Pair




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winningLotteryTicket' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY tickets as parameter.
#

def winningLotteryTicket(tickets):
    # Write your code here
    full = 2**10-1
    cntMask = [ 0 for _ in range(full+1)]
    for s in tickets:
        mask = 0 
        for c in s:
            mask |= 1 << (ord(c) - ord('0'))
        cntMask[mask] +=1
    res = 0 
    for i in range(full +1):
        for j in range(i+1, full+1):
            if i | j == full:
                res +=cntMask[i] * cntMask[j]
    res +=cntMask[full] * (cntMask[full]-1)/2
    return (int(res))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
