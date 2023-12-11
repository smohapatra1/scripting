# #   https://leetcode.com/problems/permutations-ii/
# 47. Permutations II
# Medium
# 8.2K
# 138
# Companies
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from collections import Counter
from typing import List
def permutations(nums: List[int]) -> List[List[int]]:
    res =[]
    def dfs(counter, path):
        if len(path) == len(nums):
            res.append(path)
            return 
        for x in counter:
            if counter[x]:
                counter[x] -=1
                dfs(counter, path+[x])
                counter[x] +=1
    dfs(Counter(nums), [])
    return res

if __name__ == "__main__":
    nums = [1,1,2]
    print ("{}".format(permutations(nums)))
