# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-sum-vs-xor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
# Given an integer , find each  such that:

# where  denotes the bitwise XOR operator. Return the number of 's satisfying the criteria.

# Example

# There are four values that meet the criteria:

# Return .

# Function Description

# Complete the sumXor function in the editor below.

# sumXor has the following parameter(s):
# - int n: an integer

# Returns
# - int: the number of values found

# Input Format

# A single integer, .

# Constraints

# Subtasks

#  for  of the maximum score.
# Output Format

# Sample Input 0

# 5
# Sample Output 0

# 2
# Explanation 0

# For , the  values  and  satisfy the conditions:

# Sample Input 1

# 10
# Sample Output 1

# 4
# Explanation 1

# For , the  values , , , and  satisfy the conditions:


def sumXor(n):
    if n==1:
        return 1
    c=bin(n).count('0')-1
    return 2**c

if __name__ == "__main__":
    n=int(input().strip())
    result=sumXor(n)
    print (result)