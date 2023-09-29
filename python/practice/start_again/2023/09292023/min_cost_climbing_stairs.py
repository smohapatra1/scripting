# #   https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs
# Easy
# 10.3K
# 1.6K
# Companies
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

 

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

from typing import List
def min_cost_climb(cost: List[List[int]]) -> int:
    if not cost:
        return 0
    cur=0
    dp0=cost[0]
    if len(cost) >=2:
        dp1=cost[1]
    for i in range(2, len(cost)):
        cur=cost[i] + min(dp0, dp1)
        dp0=dp1
        dp1=cur
    return min(dp0, dp1)
if __name__ == "__main__":
    #cost=[1,100,1,1,1,100,1,1,100,1]
    cost=[10,15,20]
    print ("{}".format(min_cost_climb(cost)))
