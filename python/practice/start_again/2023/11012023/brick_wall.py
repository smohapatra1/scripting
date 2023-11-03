# #   https://leetcode.com/problems/brick-wall/

# 554. Brick Wall
# Medium
# 2.4K
# 144
# Companies
# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

 

# Example 1:


# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# Example 2:

# Input: wall = [[1],[1],[1]]
# Output: 3

from collections import defaultdict
from typing import List
def brick_wall(wall: List[List[int]]) -> int:
    #Solution-01
    #Create a boundary 
    # boundary=defaultdict(int)
    # bricks_wall=len(wall)
    # for curr_brick_row in wall:
    #     curr_boundary =0
    #     for curr_brick_length in curr_brick_row[:-1]:
    #         curr_boundary +=curr_brick_length
    #         boundary[curr_boundary] +=1
    # boundary_occurrence = boundary.values()
    # if boundary_occurrence:
    #     min_crossing = bricks_wall - max(boundary_occurrence)
    # else:
    #     min_crossing = brick_wall
    # return min_crossing
    #Solution-02

    currGap= {0 : 0}
    for row in wall:
        total =0
        for brick in row[:-1]:
            total +=brick
            currGap[total] = 1+ currGap.get(total, 0)
    return len(wall) - max(currGap.values())






if __name__ == "__main__":
    #wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    wall = [[1],[1],[1]]
    print ("{}".format(brick_wall(wall)))
