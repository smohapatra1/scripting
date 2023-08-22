# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Approach :- 

# Iterate through each day, check if the current day can resolve the most recently unresolved day. 
# If it can then resolve the day, and continue checking and resolving until it finds a day it cannot resolve
# Add current day to unresolved days (stack)

def DailyTemp(tempratures):
    stack=[] # All Indices that are still unsettled 
    res=[0] * len(tempratures) # Add new days to our stacks 
    
    for i, t in enumerate(tempratures):
        while (stack and tempratures[stack[-1]] < t):
            cur = stack.pop()
            res[cur] = i - cur
        stack.append(i)
    return res

if __name__ == "__main__":
    tempratures=[73,74,75,71,69,72,76,73]
    print ("Results are {}".format(DailyTemp(tempratures)))