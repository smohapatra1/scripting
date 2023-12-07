# #   https://leetcode.com/problems/flip-equivalent-binary-trees/

# 951. Flip Equivalent Binary Trees
# Medium
# 2.2K
# 93
# Companies
# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

# Example 1:

# Flipped Trees Diagram
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
# Example 2:

# Input: root1 = [], root2 = []
# Output: true
# Example 3:

# Input: root1 = [], root2 = [1]
# Output: false
 

# Constraints:

# The number of nodes in each tree is in the range [0, 100].
# Each tree will have unique node values in the range [0, 99].

class TreeNode:
    def __init__ (self, val=0, left=None, next=None):
        self.val = val
        self.left = left
        self.next=next

def Flip_Trees(root1: TreeNode, root2 : TreeNode) -> bool:
    def dfs(match, flipper):
        if not match and not flipper:
            return True
        if not (match, flipper):
            return False
        if match.val != flipper.val:
            return False
        regular = dfs(match.left , flipper.left) and dfs(match.right, flipper.right)
        flipped=dfs(match.left, flipper.right) and dfs(match.right, flipper.left)
        return regular or flipped
    return dfs(root1, root2)
if __name__ == "__main__":
    root1 = [1,2,3,4,5,6,null,null,null,7,8]
    root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    print ("{}".format(Flip_Trees(root1, root2 )))
