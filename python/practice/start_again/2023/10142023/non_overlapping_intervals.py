# # https://leetcode.com/problems/non-overlapping-intervals/
# 35. Non-overlapping Intervals
# Medium
# 7.6K
# 201
# Companies
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


from typing import List
def non_overlapping_Intervals( intervals: List[List[int]]) -> List[int]:
    intervals=sorted(intervals, key=lambda x:x [1])
    prev=0
    count=1
    n=len(intervals)
    for i in range(1, n):
        if intervals[i][0] >=intervals[prev][1]:
            prev=i
            count +=1
    return n-count

if __name__ == "__main__":
    #intervals = [[1,2],[2,3],[3,4],[1,3]]
    intervals = [[1,2],[1,2],[1,2]]
    print ("{}".format(non_overlapping_Intervals(intervals)))
