# #   https://leetcode.com/problems/best-team-with-no-conflicts/
# 1626. Best Team With No Conflicts
# Medium
# 2.9K
# 93
# Companies
# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

# Example 1:

# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.
# Example 2:

# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
# Example 3:

# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# Explanation: It is best to choose the first 3 players. 


from typing import List
def NoConflictsTeam(scores: List[int], ages : List[int]) -> int:
    dp=[0]*(1+max(ages))
    score_ages=sorted(zip(scores, ages))
    for score, age in score_ages:
        dp[age] = score + max(dp[:age+1])
    return max(dp)


if __name__ == "__main__":
    scores = [1,3,5,10,15]
    ages = [1,2,3,4,5]
    print ("{}".format(NoConflictsTeam(scores, ages)))

