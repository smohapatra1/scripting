# #   https://www.hackerrank.com/challenges/borrowing-money/problem?isFullScreen=true

# Killgrave wants to use his mind control powers to get money from the Justice League superheroes living in  houses in Happy Harbor that are numbered sequentially from  to . There are  roads, and each road  connects two different houses,  and . Each superhero house  (where ) has  dollars stashed away for a rainy day.

# As long as a superhero is home at house , Killgrave knows they will hand over all of their saved money, . Once he gets money from them, he moves on to the next house. However, the superheroes are cunning; when Killgrave comes to house , every neighbor immediately connected to house  by a single road skips town for a couple of days (making it impossible for Killgrave to get money from them). In other words, after Killgrave visits all the superheroes he wants, there will be no road in which he was able to get money from both houses on either end of the road.

# What is the maximum amount of money Killgrave can collect from the superheroes, and how many different ways can Killgrave get that amount of money? Two ways are considered to be different if the sets of visited houses are different.

# Note: Killgrave can start at an arbitrary house and doesn't have to only use the roads.

# Input Format

# The first line contains two space-separated integers,  (the number of houses) and  (the number of roads), respectively.
# The second line contains  space-separated integers, where each integer  describes the amount of money, , at house .
# Each line  of the  subsequent lines contains two space-separated integers defining a road connecting houses  and . Every road connects a different pair of houses.

# Constraints

# , where 
# No unordered pair  will appear more than once.
# Output Format

# Print two space-separated integers:

# The first integer must denote the maximum amount of money Killgrave can get out of the Justice League.
# The second integer must denote the number of different ways he can collect that amount of money.
# Sample Input

# 3 2
# 6 8 2
# 1 2
# 3 2
# Sample Output

# 8 2
# Explanation

# happyharbor

# Killgrave has two possible courses of action:

# Visit house  and get  dollars.
# Visit houses  and  and get  dollars.
# Both of these options result in  dollars, so we know that this is maximal. Thus, we print the maximum amount of money () followed by the number of ways he can get that amount of money () as two space-separated values on a single line.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'demandingMoney' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY money
#  2. 2D_INTEGER_ARRAY roads
#

def demandingMoney(money, roads):
    # Write your code here
    x = {}
    roadSet = {i: set() for i in range(len(money))}
    for roadpair in roads:
        a = roadpair[0] - 1
        b = roadpair[1] - 1
        roadSet[a].add(b)
        roadSet[b].add(a)

    houseSet = set([i for i in range(len(money))])

    def max_money(houseSet):
        if not houseSet:
            return (0, 1)
        fsh = frozenset(houseSet)
        if fsh in x:
            return x[fsh]
        nh = houseSet.pop()
        money_a, waiting_a = max_money(houseSet - roadSet[nh])
        money_a += money[nh]
        money_b, waiting_b = max_money(houseSet)

        if money_a > money_b:
            x[fsh] = (money_a, waiting_a)
        elif money_b > money_a:
            x[fsh] = (money_b, waiting_b)
        else:
            x[fsh] = (money_a, waiting_a + waiting_b)
        return x[fsh]

    return max_money(houseSet)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    money = list(map(int, input().rstrip().split()))

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = demandingMoney(money, roads)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
