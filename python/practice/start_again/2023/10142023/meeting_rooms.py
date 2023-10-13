# #   

# Description

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), determine if a person could attend all meetings.

# Sample I/O

# Example 1

# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2

# Input: [[7,10],[2,4]]
# Output: true


from typing import List 
def meeting(intervals: List[List[int]]) -> bool:
    new_intervals=sorted(intervals, key=lambda x:x [0])
    n=len(intervals)
    for i in range(1, n ):
        if new_intervals[i-1][1] > new_intervals[i][0]:
            return False
    return True

if __name__ == "__main__":
    #intervals=[[0,30],[5,10],[15,20]]
    intervals=[[7,10],[2,4]]
    print ("{}".format(meeting(intervals)))