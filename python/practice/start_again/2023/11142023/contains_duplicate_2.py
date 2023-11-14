# #   https://leetcode.com/problems/contains-duplicate-ii/
# 219. Contains Duplicate II
# Easy
# 5.7K
# 2.9K
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

from typing import List
def duplicates(nums: List[int], k: int ) -> bool:
    index_dict = {}
    for i, n in enumerate(nums):
        if n in index_dict and i - index_dict[n] <=k:
            return True
        index_dict[n] = i 
    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    #nums = [1,2,3,1,2,3]
    #k = 2
    print ("{}".format(duplicates( nums, k )))

