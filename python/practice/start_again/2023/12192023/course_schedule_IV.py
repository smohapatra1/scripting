# #   https://leetcode.com/problems/course-schedule-iv/

# 1462. Course Schedule IV
# Medium
# 1.4K
# 63
# Companies
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

 

# Example 1:


# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.
# Example 2:

# Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites, and each course is independent.
# Example 3:


# Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]

from typing import List
def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries : List[List[int]]) -> List[bool]:
    adj={i:[] for i in range(numCourses)}

    for x,y in prerequisites:
        adj[y].append(x)
    res=[]
    def dfs(crs):
        if crs not in premap:
            premap[crs]=set()
            for nei in adj[crs]:
                premap[crs]|=dfs(nei)
        premap[crs].add(crs)
        return premap[crs]

    premap={}
    for i in range(numCourses):
        dfs(i)   
    for x,y in queries:
        res.append(x in premap[y])
    return res



if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    queries = [[0,1],[1,0]]
    print ("{}".format(checkIfPrerequisite(numCourses, prerequisites, queries)))
