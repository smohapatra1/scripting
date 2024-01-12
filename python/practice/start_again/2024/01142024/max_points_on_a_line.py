# #   https://leetcode.com/problems/max-points-on-a-line/description/

# 149. Max Points on a Line
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:


# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
 
from typing import List
from collections import defaultdict
def MaxPoints(points: List[List[int]]) -> int:
    if len(points) <=2 :
        return len(points)
    def find_slope(p1, p2):
        x1, y1 = p1
        x2, y2 = p2 
        if x1 -x2 == 0:
            return inf
        return (y2 - y1 )/(x1 -x2)
    ans = 1 
    for i, p1 in enumerate(points):
        slopes = defaultdict(int)
        for j, p2 in enumerate(points[i+1:]):
            slope=find_slope(p1, p2)
            slopes[slope] +=1
            ans = max(slopes[slope], ans)
    return ans+1


if __name__ == "__main__":
    points = [[1,1],[2,2],[3,3]]
    print ("{}".format(MaxPoints(points)))