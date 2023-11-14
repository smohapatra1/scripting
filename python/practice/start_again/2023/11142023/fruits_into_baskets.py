# #   https://leetcode.com/problems/fruit-into-baskets/

# 904. Fruit Into Baskets
# Medium
# 4.3K
# 304
# Companies
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
 
from collections import defaultdict
from typing import List
def fruitsInBaskets(fruits: List[int]) -> int:
    # Solution-01
    
    if len(fruits) < 2:
        return 1
    Max = 0
    basket = defaultdict(int)
    l=0
    for r in range(len(fruits)):
        basket[fruits[r]] +=1
        while len(basket) > 2:
            basket[fruits[l]] -=1
            if basket[fruits[l]] == 0:
                basket.pop(fruits[l])
            l+=1
        Max = max(Max, r-l +1)
    return Max

 
    # Solution-02
    # count = defaultdict(int)
    # i = 0 
    # j = 0 
    # for j in range(len(fruits)):
    #     count[fruits[j]] +=1
    #     if len(count) > 2 :
    #         count[fruits[i]] -=1
    #         if count[fruits[i]] == 0:
    #             del count[fruits[i]]
    #         i+=1
    # return j - i +1 



if __name__ == "__main__":
    #fruits = [1,2,1]
    #fruits = [1,2,3,2,2]
    fruits=[2,2,2,2,2,2,3,4,5] 
    print ("{}".format(fruitsInBaskets(fruits)))