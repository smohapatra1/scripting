# #    https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs
# Easy
# 20K
# 667
# Companies
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n:int) -> int:
    # Solution 1
    if n <=3 : return n
    dp=[0]* (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    # print (dp)
    return dp[n]
    # Solution 2
    # if n<=3: return n
    # a =(1,2)
    # for i in range(3, n+1):
    #     a = (a[1] , a[0]+ a[1])
    # return a[-1]

if __name__ == "__main__":
    n=4 # Number of steps 
    print ("{}".format(climbStairs(n)))
