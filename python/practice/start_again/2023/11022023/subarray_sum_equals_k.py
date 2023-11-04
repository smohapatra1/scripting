# #   https://leetcode.com/problems/subarray-sum-equals-k/

# 560. Subarray Sum Equals K
# Medium
# 20.2K
# 594
# Companies
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List
def subArray_sum(nums: List[int], k: int) -> int:
    ans=0
    preSum=0
    d={0:1}
    for num in nums:
        preSum +=num
        if preSum -k in d:
            ans=ans+d[preSum - k]
        d[preSum] = d.get(preSum, 0) +1
    return ans

if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    print ("{}".format(subArray_sum(nums, k )))

