# #   https://leetcode.com/problems/find-unique-binary-string/

# 1980. Find Unique Binary String
# Medium
# 1.9K
# 66
# Companies
# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 
from typing import List
def FindUnique( nums: List[int]) -> int:
    res = []
    for i in range(len(nums)):
        cur_char=nums[i][i]
        res.append('1' if cur_char == '0' else '0')
    return ''.join(res)

if __name__ == "__main__":
    nums = ["01","10"]
    print ("{}".format(FindUnique(nums)))
