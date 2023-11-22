# #   https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
# 2616. Minimize the Maximum Difference of Pairs
# Medium
# 2.2K
# 218
# Companies
# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

# Example 1:

# Input: nums = [10,1,2,7,1,3], p = 2
# Output: 1
# Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
# The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
# Example 2:

# Input: nums = [4,2,1,2], p = 1
# Output: 0
# Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
 

from typing import List
def minimizeMax(nums: List[int], p: int) -> int:
    # Solution - 01 
    # nums.sort()
    # left = 0 
    # right=nums[-1]-nums[0]
    # while left < right:
    #     mid = (left + right)//2
    #     center =0 
    #     i =0 
    #     while i<len(nums) - 1 and center < p :
    #         center, i  = ( center +1, i + 2) if nums[i+1 ] - nums[i] <=mid else (center, i+1)
    #     left, right = (left, mid) if center >= p else (mid+1, right)
    # return left

    # Solution - 02 
    nums.sort()
    n = len(nums)
    min_diff = 0 
    max_diff = nums[-1] - nums[0]
    while min_diff < max_diff:
        mid_diff = (min_diff + max_diff )//2
        count = 0 
        i = 1
        while i < n:
            if nums[i] - nums[i-1] <= mid_diff:
                count +=1
                i +=1
            i +=1
        if count >= p:
            max_diff = mid_diff
        else:
            min_diff = mid_diff +1 
    return min_diff




if __name__ == "__main__":
    nums = [10,1,2,7,1,3]
    p = 2
    print ("{}".format(minimizeMax(nums, p)))