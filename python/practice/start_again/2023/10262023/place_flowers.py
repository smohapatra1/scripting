# #   https://leetcode.com/problems/can-place-flowers/

# 605. Can Place Flowers
# Easy
# 5.9K
# 1K
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

from typing import List
def place_flowers(flower: List[int], n: int) -> bool:
    a=len(flower)
    if n== 0:
        return True
    for i in range(a):
        if flower[i] == 0 and (i==0 or flower[i-1] == 0) and (i==len(flower)-1 or flower[i+1]==0):
            flower[i] = 1
            n-=1
            if n==0:
                return True
    return False

if __name__ == "__main__":
    #flower = [1,0,0,0,1]
    #n = 1
    flower = [1,0,0,0,1]
    n = 2
    print ("{}".format(place_flowers(flower, n)))
