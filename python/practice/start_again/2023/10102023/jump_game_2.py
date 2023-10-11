# # https://leetcode.com/problems/jump-game-ii/
# 45. Jump Game II
# Medium
# 13.5K
# 481
# Companies
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

from typing import List
def jumpGame2(nums: List[int]) -> int:
    start=0
    count=0
    last=0
    for i in range(len(nums)-1):
        start=max(start, i + nums[i])
        if i == last:
            last = start
            count+=1
    return count 

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print ("{}".format(jumpGame2(nums)))

