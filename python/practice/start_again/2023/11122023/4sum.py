# #   https://leetcode.com/problems/4sum/

# 18. 4Sum
# Medium
# 10.7K
# 1.3K
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

from typing import List
def sum4(nums: List[int], target: int) -> List[int]:
    ans=set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            k = j+1
            l=len(nums)-1
            while k < l:
                s =nums[i] + nums[j] + nums [k] + nums[l]
                if s == target:
                    ans.add((nums[i], nums[j], nums[k], nums[l]))
                    l-=1
                    k+=1
                elif s > target:
                    l-=1
                else:
                    k+=1
    return ans



if __name__ == "__main__":
    #nums = [1,0,-1,0,-2,2]
    #target = 0
    nums = [2,2,2,2,2]
    target = 8
    print ("{}".format(sum4(nums, target)))


