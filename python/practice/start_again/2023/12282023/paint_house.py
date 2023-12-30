

# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0256.Paint%20House/README_EN.md

# Description

# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.

 

# Example 1:

# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.
# Example 2:

# Input: costs = [[7,6,2]]
# Output: 2


from typing import List

def PaintHouse( costs: List[List[int]]) -> int:
    a = b = c =0
    for ca, cb, cc in costs:
        a , b, c =  min(b, c ) + ca , min(a, c) + cb, min(a, b) + cc
    return min(a,b,c)



if __name__ == "__main__":
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print ("{}".format(PaintHouse(costs)))