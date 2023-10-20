#  1929. Concatenation TWO Array
# Easy
# 2.9K
# 337
# Companies
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums1 = [1,2,1] nums2 = [3,4,5]
# Output: [1,2,1,3,4,5]

from typing import List
def concatenate_array(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 +=nums2
    return nums1

if __name__ == "__main__":
    nums1 = [1,2,1] 
    nums2 = [3,4,5]
    print ("{}".format(concatenate_array(nums1, nums2)))

