# #   https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

# 698. Partition to K Equal Sum Subsets
# Medium
# 6.9K
# 489
# Companies
# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false
 
from typing import List
def partitionKSubset( nums: List[int], K: int) -> bool:
    total = sum(nums)
    if total % k:
        return False

    reqSum = total // k
    subSets = [0] * k
    nums.sort(reverse = True)

    def recurse(i):
        if i == len(nums):    
            return True

        for j in range(k):
            if subSets[j] + nums[i] <= reqSum:
                subSets[j] += nums[i]

                if recurse(i + 1):
                    return True

                subSets[j] -= nums[i]
                if subSets[j] == 0:
                    break

        return False

    return recurse(0)


if __name__ == "__main__":
    nums = [4,3,2,3,5,2,1]
    k = 4
    print ("{}".format(partitionKSubset(nums, k )))
