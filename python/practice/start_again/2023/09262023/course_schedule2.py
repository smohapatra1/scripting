# #   https://leetcode.com/problems/course-schedule-ii/
# 210. Course Schedule II
# Medium
# 10K
# 317
# Companies
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]


from typing import List
from collections import deque 
from collections import defaultdict

def courseSchedule2(numCourse: int, prerequisites: List[List[int]]) -> List[int]:
    topcourse=[]
    preq={i: set() for i in range(numCourse)}
    graph=defaultdict(set)
    for i , j in prerequisites:
        preq[i].add(j)
        graph[j].add(i)
    q=deque([k for k, v in preq.items() if not v ])
    while q:
        course=q.popleft()
        topcourse.append(course)
        if len(topcourse) == numCourse:
            return topcourse
        for cor in graph[course]:
            preq[cor].remove(course)
            if not preq[cor]:
                q.append(cor)
    return []
if __name__ == "__main__":
    numCourse = 2
    prerequisites = [[1,0]]
    print ("{}".format(courseSchedule2(numCourse , prerequisites)))

