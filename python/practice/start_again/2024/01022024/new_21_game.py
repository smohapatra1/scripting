# #   https://leetcode.com/problems/new-21-game/
# 837. New 21 Game
# Medium
# 1.9K
# 1.8K
# Companies
# Alice plays the following game, loosely based on the card game "21".

# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

# Alice stops drawing numbers when she gets k or more points.

# Return the probability that Alice has n or fewer points.

# Answers within 10-5 of the actual answer are considered accepted.

 

# Example 1:

# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000
# Explanation: Alice gets a single card, then stops.
# Example 2:

# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.
# Example 3:

# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278

def New21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0:
        return 1.0
    if n >=k-1 + maxPts:
        return 1.0
    dp=[0.0] * (n+1)
    dp[0] = 1.0
    probability = 0.0
    windowSum=1.0
    for i in range(1, n+1):
        dp[i] = windowSum/maxPts
        if i < k:
            windowSum +=dp[i]
        else:
            probability +=dp[i]
        if i >= maxPts:
            windowSum -=dp[i- maxPts]
    return probability
    

if __name__ == "__main__":
    n = 10
    k = 1
    maxPts = 10
    print ("{}".format(New21Game(n, k, maxPts)))