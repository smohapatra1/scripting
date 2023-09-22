# #   https://leetcode.com/problems/subsets-ii/
# 90. Subsets II
# Medium
# 9K
# 254
# Companies
# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

from typing import List
def subsets2( nums: List[int]) -> List[List[int]]:
    n=len(nums)
    subsets=[]
    nums.sort()
    def dfs(idx, path):
        subsets.append(path)
        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue
            dfs(i+1, path+ [nums[i]])
    dfs(0, [])
    return subsets

if __name__ == "__main__":
    nums = [1,2,2]
    print ("{}".format(subsets2(nums)))



