# #   https://leetcode.com/problems/counting-bits/
# 338. Counting Bits
# Easy
# 10.6K
# 481
# Companies
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

from typing import List
def counting_bits(n: int) -> List[int]:
    #Solution-01
    # counter=[0]
    # for i in range(1, n+1):
    #     counter.append(counter[i>>1] + i % 2)
    # return counter
    #Solution - 02 
    return [bin(i).count('1') for i in range(n+1)]


if __name__ == "__main__":
    n=5
    print ("{}".format(counting_bits(n)))
