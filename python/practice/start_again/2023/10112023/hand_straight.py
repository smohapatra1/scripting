# #   https://leetcode.com/problems/hand-of-straights/

# 846. Hand of Straights
# Medium
# 2.4K
# 159
# Companies
# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

from typing import List
from collections import Counter
def straight_hand(hand : List[int], groupSize: int) -> bool:
    if len(hand)%groupSize != 0:
        return False
    dic=Counter(hand)
    keys=sorted(dic.keys())
    for k in keys:
        f=dic[k]
        if f !=0:
            for j in range(1, groupSize):
                if dic[k+j] < f:
                    return False
                dic[k+j] -=1
    return True 

if __name__ == "__main__":
    # hand = [1,2,3,6,2,3,4,7,8]
    # #hand=[1,2]
    # groupSize = 3
    hand = [1,2,3,4,5]
    groupSize = 4
    print ("{}".format(straight_hand(hand, groupSize)))
