# #   https://leetcode.com/problems/find-peak-element/

# 162. Find Peak Element
# Medium
# 10.9K
# 4.5K
# Companies
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


from typing import List
def findPeak ( nums: List[int]) -> int:
    if nums == 0:
        return 0 
    left = 1
    right = len(nums) -1  
    while left < right:
        mid = left + (right - left + 1 )//2
        if nums[mid] < nums[mid -1 ]:
            right = mid -1 
        else:
            left = mid
    return left

if __name__ == "__main__":
    #nums = [1,2,3,1]
    nums = [1,2,1,3,5,6,4]
    print ("From nums {}, the peak one is {}".format(nums, findPeak(nums)))
