# #   https://leetcode.com/problems/remove-covered-intervals/description/


# 1288. Remove Covered Intervals
# Medium

# Topics
# Companies

# Hint
# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.

 

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1

from typing import List
def Intervals(intervals: List[List[int]]) -> int:
    interval=sorted(intervals, key=lambda x: (x[0], -x[1]))
    res=0
    ended=0
    for _, end  in interval:
        if end > ended:
            res +=1
            ended = end
    return res


if __name__ == "__main__":
    intervals = [[1,4],[3,6],[2,8]]
    print ("{}".format(Intervals(intervals)))