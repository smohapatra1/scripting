#   https://leetcode.com/problems/permutations/
#   
# 46. Permutations
# Medium
# 17.9K
# 290
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.


from typing import List
def permutation(nums: List[int] ) -> List[List[int]]:
    def backtrack(nums, path):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
    result =[]
    backtrack(nums, [])
    return result

if __name__ == "__main__":
    nums = [1,2,3]
    print ("{}".format(permutation(nums)))



