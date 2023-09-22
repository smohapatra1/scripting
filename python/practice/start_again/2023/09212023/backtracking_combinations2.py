#   https://leetcode.com/problems/combination-sum-ii/

# 40. Combination Sum II
# Medium
# 9.6K
# 245
# Companies
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

from typing import List
import collections
def combinations2(candidates: List[int], target: int) -> List[List[int]]:
    result=[]
    candidates.sort()
    def dfs(idx, path, curr):
        if curr > target :
            return 
        if curr == target:
            result.append(path)
            return 
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            dfs(i+1, path + [candidates[i]], curr + candidates[i])
    dfs(0, [],0)
    return result

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print ("{}".format(combinations2(candidates, target)))



