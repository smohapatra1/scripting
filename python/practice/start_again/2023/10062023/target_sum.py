#   https://leetcode.com/problems/target-sum/

# 494. Target Sum
# Medium
# 10.2K
# 330
# Companies
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1
from typing import List
import collections
def target_sum(nums: List[int], target: int) -> int :
    if not nums or sum(nums) < target:
        return 0
    dict={0:1}
    for i in range(len(nums)):
        temp_dict=collections.defaultdict(int)
        for k in dict:
            temp_dict[k+nums[i]] +=dict[k]
            temp_dict[k-nums[i]] +=dict[k]
        dict=temp_dict
    return dict[target]

if __name__ == "__main__":
    #nums = [1,1,1,1,1]
    #target = 3
    nums = [1]
    target = 1
    print ("{}".format(target_sum(nums, target)))