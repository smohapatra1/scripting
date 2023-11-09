# #   https://leetcode.com/problems/number-of-zero-filled-subarrays/  

# 2348. Number of Zero-Filled Subarrays
# Medium
# 2.2K
# 72
# Companies
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
# Example 2:

# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
# Example 3:

# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.
 

from typing import List
def sumarryas( nums: list[int]) -> int:
    total_sub_zeros = curr_sub_zeros = 0 
    for num in nums:
        if num == 0 :
            curr_sub_zeros +=1
            total_sub_zeros +=curr_sub_zeros
        else:
            curr_sub_zeros = 0 
    return total_sub_zeros


if __name__ == "__main__":
    #nums = [0,0,0,2,0,0]
    nums = [1,3,0,0,2,0,0,4]
    print ("{}".format(sumarryas(nums)))