# 207. Course Schedule
# Medium
# 15.2K
# 605
# Companies
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

from typing import List
from collections import deque
def course_schedule(numCourses : int, prerequisites: List[List[int]]) -> bool:
    adj=[[] for _ in range(numCourses)]
    degree= [0] * numCourses
    for (curr, pre) in prerequisites:
        adj[pre].append(curr)
        degree[curr] +=1
    queue=deque(i for (i,d) in enumerate(degree) if d == 0)
    visited=0
    while queue:
        curr=queue.popleft()
        visited +=1
        for dep in adj[curr]:
            degree[dep] -=1
            if not degree[dep]:
                queue.append(dep)
    return visited == numCourses

if __name__ == "__main__":
    #numCourses = 2
    #prerequisites = [[1,0]]
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print ("{}".format(course_schedule(numCourses, prerequisites)))



