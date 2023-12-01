# #   https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# 108. Convert Sorted Array to Binary Search Tree
# Easy
# 10.5K
# 526
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
from anytree import Node, RenderTree , TreeNode
from typing import List
def sortedArrayToBST( nums: List[int]) -> List:
    if len(nums) == 0:
        return None
    mid = len(nums)//2
    root=TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right= sortedArrayToBST(nums[mid+1:])
    return root


if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    print ("{}".format(sortedArrayToBST( nums)))
