# #   https://leetcode.com/problems/insert-interval/
# 57. Insert Interval
# Medium
# 9.1K
# 663
# Companies
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

from typing import List
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    for interval in intervals:
        # if New interval is after range of interval 
        if interval[1] < newInterval[0]:
            result.append(interval)
        # If new interval range is before the interval 
        elif interval [0] > newInterval[1]:
            result.append(newInterval)
            newInterval = interval
        # If we have an overlap 
        elif interval [0] <= newInterval[1] or interval[1] >= newInterval[0]:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max ( interval[1], newInterval[1])
    result.append(newInterval)
    return result 

if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print ("{}".format(insert(intervals, newInterval)))

