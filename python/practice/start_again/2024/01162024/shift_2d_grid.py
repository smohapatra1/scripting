# #   https://leetcode.com/problems/shift-2d-grid/description/

# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

 

# Example 1:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
# Example 2:


# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# Example 3:

# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]

from typing import List
def Shift2d(grid: List[List[int]], k: int ) -> List[int]:
    col=len(grid[0])
    nums = sum(grid, [])
    k = k % len(nums)
    nums = nums[-k:] + nums[:-k]
    return [nums[i:i+col] for i in range(0, len(nums), col)]

if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    print ("{}".format(Shift2d(grid, k)))
    
