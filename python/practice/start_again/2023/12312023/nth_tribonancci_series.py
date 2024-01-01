# #   https://leetcode.com/problems/n-th-tribonacci-number/
# 1137. N-th Tribonacci Number
# Easy
# 4K
# 173
# Companies
# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537

import collections
def Tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n ==1 or n ==2 :
        return 1
    return Tribonacci(n-1) + Tribonacci(n-2) + Tribonacci(n-3)
    return Tribonacci(n)



if __name__ == "__main__":
    n=4
    print("{}".format(Tribonacci(n)))