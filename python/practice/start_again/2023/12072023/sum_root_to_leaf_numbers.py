# #   https://leetcode.com/problems/sum-root-to-leaf-numbers/
# 129. Sum Root to Leaf Numbers
# Medium
# 7.3K
# 117
# Companies
# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:


# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
 
class TreeNode:
    def __init__(self, val=0, left=None, next=None):
        self.val = val
        self.next = next
        self.left = left
def sumNumbers(root: TreeNode) -> int:
    def dfs(curr, num):
        if curr is None:
            return 0
        num = num* 10+curr.val
        if not curr.left and not curr.right:
            return num
        return dfs(curr.left, num)+dfs(curr.right, num)
    return dfs(root, 0)



if __name__ == "__main__":
    root = [1,2,3]
    print ("{}".format(sumNumbers(root)))