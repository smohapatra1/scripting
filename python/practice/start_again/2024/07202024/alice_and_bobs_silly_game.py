# #   https://www.hackerrank.com/challenges/alice-and-bobs-silly-game/problem?isFullScreen=true

# Alice and Bob invented the following silly game:

# The game starts with an integer, , that's used to build a  of  distinct integers in the inclusive range from  to  (i.e., ).
# Alice always plays first, and the two players move in alternating turns.
# During each move, the current player chooses a prime number, , from . The player then removes  and all of its multiples from .
# The first player to be unable to make a move loses the game.
# Alice and Bob play  games. Given the value of  for each game, print the name of the game's winner on a new line. If Alice wins, print Alice; otherwise, print Bob.

# Note: Each player always plays optimally, meaning they will not make a move that causes them to lose the game if some better, winning move exists.

# Input Format

# The first line contains an integer, , denoting the number of games Alice and Bob play.
# Each line  of the  subsequent lines contains a single integer, , describing a game.

# Constraints

# Subtasks

#  for  of the maximum score
# Output Format

# For each game, print the name of the winner on a new line. If Alice wins, print Alice; otherwise, print Bob.

# Sample Input 0

# 3
# 1
# 2
# 5
# Sample Output 0

# Bob
# Alice
# Alice
# Explanation 0

# Alice and Bob play the following  games:

# We are given , so . Because Alice has no valid moves (there are no prime numbers in the set), she loses the game. Thus, we print Bob on a new line.
# We are given , so . Alice chooses the prime number  and deletes it from the set, which becomes . Because Bob has no valid moves (there are no prime numbers in the set), he loses the game. Thus, we print Alice on a new line.
# We are given , so . Alice chooses the prime number  and deletes the numbers  and  from the set, which becomes . Now there are two primes left,  and . Bob can remove either prime from the set, and then Alice can remove the remaining prime. Because Bob is left without a final move, Alice will always win. Thus, we print Alice on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sillyGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
primes = [2]

def isPrime(x):
        for i in range(2, int(x ** .5) + 1):
            if not x % i: return False
        return True

def sillyGame(n):
    # Write your code here
    biggest_prime = primes[-1]
    if n > biggest_prime:
        for i in range(biggest_prime + 1, n + 1):
            if isPrime(i): primes.append(i)
    return 'Alice' if sum(i <= n for i in primes) % 2 else 'Bob'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        result = sillyGame(n)

        fptr.write(result + '\n')

    fptr.close()
