# #   https://leetcode.com/problems/house-robber-iii/
# 337. House Robber III
# Medium
# 8.3K
# 135
# Companies
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

# Example 1:


# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:


# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

class TreeNode:
     def __init__(self, val=0, left=None, next=None):
          self.val = val
          self.next=next
          self.left=left
def rob( root: TreeNode) -> int:
    return max(self.dfs(root))
def dfs (self, root: TreeNode):
    if not root:
         return (0, 0)
    left = self.dfs(root.left)
    right=self.dfs(root.right)
    return (root.val + left[1]+ right[1], max(left[0], left[1]) + max(right[0], right[1]))

     
     

if __name__ == "__main__":
     root = [3,2,3,3,1]
     print ("{}".format(rob(root)))