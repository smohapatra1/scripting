# #   https://leetcode.com/problems/ones-and-zeroes/

# 474. Ones and Zeroes
# Medium
# 5.3K
# 441
# Companies
# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

 

# Example 1:

# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
# Example 2:

# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 
from typing import List
def OnesAndZeros(strs: List[int], m: int, n: int)-> int:
    dp=[[0] * (n+1) for _ in range(m+1)]
    counter=[[s.count("0"), s.count("1")] for s in strs]
    for zeros, ones in counter:
        for i in range(m, zeros -1, -1):
            for j in range(n, ones-1, -1):
                dp[i][j] = max(dp[i][j], 1+dp[i-zeros][j-ones])
    return dp[-1][-1]


if __name__ == "__main__":
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    print ("{}".format(OnesAndZeros(strs, m, n)))
