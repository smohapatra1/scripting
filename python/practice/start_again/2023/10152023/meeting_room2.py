# # https://zhenyu0519.github.io/2020/07/13/lc253/

# Description

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number of conference rooms required.

# Sample I/O

# Example 1

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2

# Input: [[7,10],[2,4]]
# Output: 1


from typing import List
def meeting2(intervals: List[List[int]]) -> int:
    
    n=len(intervals)
    if n <=1:
        return n
    new_intervals=sorted(intervals)
    rooms=[[new_intervals[0][1]]]
    for i in range(1, n ):
        booked=False
        for room in rooms:
            if new_intervals[i][0] >= room[-1]:
                room.append(new_intervals[i][1])
                booked=True
                break
        if not booked:
            rooms.append([new_intervals[i][1]])
    return len(rooms)

if __name__ == "__main__":
    #intervals=[[0, 30],[5, 10],[15, 20]]
    intervals=[[7,10],[2,4]]
    print ("{}".format(meeting2(intervals)))
