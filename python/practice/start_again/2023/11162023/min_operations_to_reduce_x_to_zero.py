# #   https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

# 1658. Minimum Operations to Reduce X to Zero
# Medium
# 5.3K
# 112
# Companies
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


from typing import List
def minOperations( nums: List[int], x: int) -> int:
    target = sum(nums) - x
    n=len(nums)
    if target == 0 :
        return n
    max_len = curr_sum = left = 0
    for right, val in enumerate(nums):
        curr_sum +=val
        while left <=right and curr_sum > target:
            curr_sum -=nums[left]
            left +=1
        if curr_sum == target:
            max_len = max(max_len, right - left +1 )
    return n - max_len if max_len else -1 

if __name__ == "__main__":
     #nums = [1,1,4,2,3]
     #x = 5
     nums = [3,2,20,1,1,3]
     x = 10
     print ("{}".format(minOperations(nums, x )))
