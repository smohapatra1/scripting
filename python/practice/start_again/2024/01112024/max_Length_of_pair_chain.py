# #   https://leetcode.com/problems/maximum-length-of-pair-chain/description/

# 646. Maximum Length of Pair Chain
# Medium

# Topics
# Companies
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

# Return the length longest chain which can be formed.

# You do not need to use up all the given intervals. You can select pairs in any order.

 

# Example 1:

# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# Example 2:

# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 
from typing import List
def MaxLengthChain( pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda x:x[1])
    curr = float('-inf')
    ans = 0 
    for pair in pairs:
        if curr < pair[0]:
            curr = pair[1]
            ans +=1
    return ans

if __name__ == "__main__":
    pairs = [[1,2],[2,3],[3,4]]
    print ("{}".format(MaxLengthChain(pairs)))

