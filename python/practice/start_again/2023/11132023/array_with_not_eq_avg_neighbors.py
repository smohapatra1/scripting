# #   https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

# 1968. Array With Elements Not Equal to Average of Neighbors
# Medium
# 552
# 38
# Companies
# You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

# More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

# Return any rearrangement of nums that meets the requirements.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: [1,2,4,5,3]
# Explanation:
# When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
# When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
# When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
# Example 2:

# Input: nums = [6,2,0,9,7]
# Output: [9,7,6,2,0]
# Explanation:
# When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
# When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
# When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
 
from typing import List
def rearrangeArray( nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if i % 2:
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        else:
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
    return nums


if __name__ == "__main__":
    #nums = [1,2,3,4,5]
    nums = [6,2,0,9,7]
    print ("{}".format(rearrangeArray(nums)))
