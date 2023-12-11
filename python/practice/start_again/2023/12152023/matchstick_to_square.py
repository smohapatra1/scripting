# #   https://leetcode.com/problems/matchsticks-to-square/

# 473. Matchsticks to Square
# Medium
# 3.7K
# 282
# Companies
# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.

from typing import List
def MatchStick(matchsticks: List[int]) -> bool:
    total=sum(matchsticks)
    if total % 4:
        return False
    reqLen=total //4
    sides=[0] * 4
    matchsticks.sort(reverse=True)
    def recursive(i):
        if i == len(matchsticks):
            return True
        for j in range(4):
            if sides[j] + matchsticks[i] <=reqLen:
                sides[j] +=matchsticks[i]
                if recursive(i+1):
                        return True
                sides[j] -=matchsticks[i]
                if sides[j] == 0:
                        break
        return False
    return recursive(0)
            



if __name__ == "__main__":
     matchsticks = [1,1,2,2,2]
     print ("{}".format(matchsticks))

