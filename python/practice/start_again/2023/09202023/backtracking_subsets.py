#   https://neetcode.io/practice
# #   https://leetcode.com/problems/subsets/
# 78. Subsets
# Medium
# 15.8K
# 232
# Companies
# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


from typing import List

def subsets ( nums:List[int] ) -> List[List[int]]:
    n = len(nums)
    subsets=[]
    for mask in range(1<<n):
        subset=[]
        for i in range(n):
            if mask & (1 << i ):
                subset.append(nums[i])
        subsets.append(subset)
    return subsets

if __name__ == "__main__":
    #nums = [1,2,3]
    nums= [0]
    print ("{}".format(subsets(nums)))

