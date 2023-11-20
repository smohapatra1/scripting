# #   https://leetcode.com/problems/search-insert-position/
# 35. Search Insert Position
# Easy
# 15.1K
# 658
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
import bisect
from typing import List 
def searchInsert( nums : List[int], target: int ) -> int:
    # Solution-01
    return bisect.bisect_left(nums, target)
    
    #Solution-02
    # if not nums:
    #     return 0
    # for i, j in enumerate(nums):
    #     if j >= target:
    #         return i
    # return len(nums)


if __name__ == "__main__":
    #nums=[1,3,5,6]
    #target=5
    #nums = [1,3,5,6]
    #target = 7
    nums = [1,3,5,6]
    target = 2
    print ("{}".format(searchInsert(nums, target)))