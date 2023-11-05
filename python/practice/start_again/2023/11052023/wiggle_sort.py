#   https://leetcode.com/problems/wiggle-sort/

#   https://zhenyu0519.github.io/2020/07/12/lc280/

# Description

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]….

# Sample I/O

# Example 1

# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]
# Methodology

# Create a flag to indicate the condition is cur >= next or cur <= next. Iterate the given input, if the condition suppose to be cur >= next but cur <= next then swap the cur and next; if the condition suppose to be cur <= next but cur >= next then swap the cur and next. For each iteration, the flag need to flip.

# Another solution is sort the given input first. Then swap two adjacent elements based on the index. This gives O(n) time complexity as well.

from typing import List
def wiggle_sort(nums: List[int]) -> List[int]:
    greater=False
    for i in range(len(nums)-1):
        if ( greater and nums[i] <=nums[i+1]) or (not greater and nums[i]>=nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        greater = not greater
    return nums


if __name__ == "__main__":
    nums = [3,5,2,1,6,4]
    print ("{}".format(wiggle_sort(nums)))