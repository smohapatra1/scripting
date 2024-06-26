# https://www.hackerrank.com/challenges/maximizing-xor/problem?isFullScreen=true

# Given two integers,  and , find the maximal value of  xor , written , where  and  satisfy the following condition:


# For example, if  and , then



# Our maximum value is .

# Function Description

# Complete the maximizingXor function in the editor below. It must return an integer representing the maximum value calculated.

# maximizingXor has the following parameter(s):

# l: an integer, the lower bound, inclusive
# r: an integer, the upper bound, inclusive
# Input Format

# The first line contains the integer .
# The second line contains the integer .

# Constraints

# 3

# Output Format

# Return the maximal value of the xor operations for all permutations of the integers from  to , inclusive.

# Sample Input 0

# 10
# 15
# Sample Output 0

# 7
# Explanation 0

# Here  and . Testing all pairs:






















# Two pairs, (10, 13) and (11, 12) have the xor value 7, and this is maximal.

# Sample Input 1

# 11
# 100
# Sample Output 1

# 127


def maximizingOr(l, r):
    m = 0 
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            xor = i ^ j
            if xor > m:
                m = xor
    return m

if __name__ == "__main__":
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingOr(l, r)
    print (result)