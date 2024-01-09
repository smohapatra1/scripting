# #   https://leetcode.com/problems/jump-game-vii/


# 1871. Jump Game VII
# Medium
# 1.6K
# 92
# Companies
# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

 

# Example 1:

# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.
# Example 2:

# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
 

def JumpGameVII(s: str, minJump : int, maxJump: int ) -> bool:
    if s[-1] == '1' :
        return False
    n=len(s)
    end = minJump
    reach = [True] + [False] * (n-1)
    for i in range(n):
        if reach[i]:
            start = max(i+ minJump, end)
            end=min(i + maxJump+1, n )
            for j in range(start, end):
                if s[j] == '0':
                    reach[j] = True
            if end == n:
                return reach[-1]
    return reach[-1]
if __name__ == "__main__":
    s = "011010"
    minJump = 2
    maxJump = 3
    # s = "01101110"
    # minJump = 2
    # maxJump = 3
    print ("{}".format(JumpGameVII(s, minJump, maxJump)))