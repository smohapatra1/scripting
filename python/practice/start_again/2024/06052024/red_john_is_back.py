# #   https://www.hackerrank.com/challenges/red-john-is-back/problem?isFullScreen=true

# Red John has committed another murder. This time, he doesn't leave a red smiley behind. Instead he leaves a puzzle for Patrick Jane to solve. He also texts Teresa Lisbon that if Patrick is successful, he will turn himself in. The puzzle begins as follows.

# There is a wall of size 4xn in the victim's house. The victim has an infinite supply of bricks of size 4x1 and 1x4 in her house. There is a hidden safe which can only be opened by a particular configuration of bricks. First we must calculate the total number of ways in which the bricks can be arranged so that the entire wall is covered. The following diagram shows how bricks might be arranged to cover walls where :

# image

# There is one more step to the puzzle. Call the number of possible arrangements . Patrick must calculate the number of prime numbers  in the inclusive range .

# As an example, assume . From the diagram above, we determine that there is only one configuration that will cover the wall properly.  is not a prime number, so .

# A more complex example is . The bricks can be oriented in  total configurations that cover the wall. The two primes  and  are less than or equal to , so .

# image

# Function Description

# Complete the redJohn function in the editor below. It should return the number of primes determined, as an integer.

# redJohn has the following parameter(s):

# n: an integer that denotes the length of the wall
# Input Format

# The first line contains the integer , the number of test cases.
# Each of the next  lines contains an integer , the length of the  wall.

# Constraints

# Output Format

# Print the integer  on a separate line for each test case.

# Sample Input

# 2
# 1
# 7
# Sample Output

# 0
# 3
# Explanation

# For , the brick can be laid in 1 format only: vertically.


# The number of primes  is .

# For , one of the ways in which we can lay the bricks is

# Red John

# There are  ways of arranging the bricks for  and there are  primes .


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'redJohn' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def redJohn(n):
    # Write your code here
    ways = [0, 1,1,1,2] + [0]*(n-4)
    for i in range(5, n+1):
        ways[i] += ways[i-1] + ways[i-4]
    return primes_bellow(ways[n])
def primes_bellow(k):
    count = 0 
    for p in range(2, k+1):
        is_prime = True 
        for i in range(2, int(p**0.5)+1):
            if p % i == 0:
                is_prime = False
                break
        if is_prime:
            count +=1
    return count
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
